"""Knowledge Base Manager for vector storage and retrieval."""

import uuid
from datetime import datetime
from typing import Any, Optional

from src.knowledge_base.chunker import DocumentChunker
from src.models.documents import DocumentMetadata, IndexedChunk, ParsedDocument
from src.models.enums import Language
from src.models.search import SearchResult
from src.nlp.embeddings import EmbeddingGenerator


class KnowledgeBaseManager:
    """
    Manage vector storage, indexing, and semantic search.

    Uses Qdrant as the vector database backend with support for
    metadata filtering and bilingual (Arabic/English) content.
    """

    COLLECTION_NAME = "engineering_documents"
    VECTOR_SIZE = 384  # Default for sentence-transformers

    def __init__(
        self,
        qdrant_url: str = "http://localhost:6333",
        qdrant_api_key: Optional[str] = None,
        collection_name: Optional[str] = None,
        embedding_generator: Optional[EmbeddingGenerator] = None,
    ):
        """
        Initialize the Knowledge Base Manager.

        Args:
            qdrant_url: Qdrant server URL
            qdrant_api_key: Optional API key for Qdrant Cloud
            collection_name: Name of the collection to use
            embedding_generator: Custom embedding generator
        """
        self.qdrant_url = qdrant_url
        self.qdrant_api_key = qdrant_api_key
        self.collection_name = collection_name or self.COLLECTION_NAME

        self.embedding_generator = embedding_generator or EmbeddingGenerator()
        self.chunker = DocumentChunker()

        self._client = None
        self._models = None
        self._initialize_client()

    def _initialize_client(self):
        """Initialize Qdrant client."""
        try:
            from qdrant_client import QdrantClient
            from qdrant_client import models

            self._models = models

            if self.qdrant_api_key:
                self._client = QdrantClient(
                    url=self.qdrant_url,
                    api_key=self.qdrant_api_key,
                )
            else:
                self._client = QdrantClient(url=self.qdrant_url)

            # Ensure collection exists
            self._ensure_collection()

        except ImportError:
            # Qdrant client not available - use in-memory fallback
            self._client = None
            self._in_memory_store: dict[str, IndexedChunk] = {}

    def _ensure_collection(self):
        """Ensure the collection exists in Qdrant."""
        if self._client is None:
            return

        try:
            collections = self._client.get_collections().collections
            collection_names = [c.name for c in collections]

            if self.collection_name not in collection_names:
                self._client.create_collection(
                    collection_name=self.collection_name,
                    vectors_config=self._models.VectorParams(
                        size=self.VECTOR_SIZE,
                        distance=self._models.Distance.COSINE,
                    ),
                )
        except Exception:
            pass

    def index_document(
        self,
        document: ParsedDocument,
        metadata: Optional[DocumentMetadata] = None,
    ) -> str:
        """
        Index a parsed document into the knowledge base.

        Args:
            document: Parsed document to index
            metadata: Optional metadata override

        Returns:
            Document ID
        """
        # Use provided metadata or document's metadata
        doc_metadata = metadata or document.metadata

        # Generate document ID if not set
        if not doc_metadata.document_id:
            doc_metadata.document_id = str(uuid.uuid4())

        document.metadata = doc_metadata

        # Chunk the document
        chunks = self.chunker.chunk_document(document)

        # Generate embeddings for each chunk
        for chunk in chunks:
            language = Language(chunk.metadata.get("language", "en"))
            embedding_result = self.embedding_generator.generate(
                chunk.content, language
            )
            chunk.embedding = embedding_result.vector.tolist()

            # Add document metadata to chunk metadata
            chunk.metadata.update({
                "document_id": doc_metadata.document_id,
                "filename": doc_metadata.filename,
                "project_type": doc_metadata.project_type.value if doc_metadata.project_type else None,
                "client": doc_metadata.client,
                "discipline": doc_metadata.discipline.value if doc_metadata.discipline else None,
                "date": doc_metadata.date.isoformat() if doc_metadata.date else None,
            })

        # Store chunks
        self._store_chunks(chunks)

        return doc_metadata.document_id


    def _store_chunks(self, chunks: list[IndexedChunk]):
        """Store chunks in vector database."""
        if self._client is None:
            # In-memory fallback
            for chunk in chunks:
                self._in_memory_store[chunk.chunk_id] = chunk
            return

        try:
            points = []
            for chunk in chunks:
                point = self._models.PointStruct(
                    id=chunk.chunk_id,
                    vector=chunk.embedding,
                    payload={
                        "content": chunk.content,
                        "document_id": chunk.document_id,
                        "start_char": chunk.start_char,
                        "end_char": chunk.end_char,
                        **chunk.metadata,
                    },
                )
                points.append(point)

            self._client.upsert(
                collection_name=self.collection_name,
                points=points,
            )
        except Exception as e:
            # Fallback to in-memory
            for chunk in chunks:
                self._in_memory_store[chunk.chunk_id] = chunk

    def search(
        self,
        query: str,
        top_k: int = 10,
        filters: Optional[dict[str, Any]] = None,
        language: Optional[Language] = None,
    ) -> list[SearchResult]:
        """
        Perform semantic search across the knowledge base.

        Args:
            query: Search query text
            top_k: Number of results to return
            filters: Optional metadata filters
            language: Query language (auto-detected if not provided)

        Returns:
            List of SearchResult objects
        """
        # Generate query embedding
        if language is None:
            from src.ingestion.language_detector import LanguageDetector
            detector = LanguageDetector()
            language = detector.detect(query)

        query_embedding = self.embedding_generator.generate(query, language)

        if self._client is None:
            # In-memory search
            return self._in_memory_search(query_embedding.vector, top_k, filters)

        try:
            # Build Qdrant filter
            qdrant_filter = self._build_filter(filters) if filters else None

            results = self._client.search(
                collection_name=self.collection_name,
                query_vector=query_embedding.vector.tolist(),
                limit=top_k,
                query_filter=qdrant_filter,
            )

            return [
                SearchResult(
                    chunk_id=str(r.id),
                    document_id=r.payload.get("document_id", ""),
                    content=r.payload.get("content", ""),
                    score=r.score,
                    metadata={k: v for k, v in r.payload.items() if k != "content"},
                    document_metadata=None,
                )
                for r in results
            ]

        except Exception:
            return self._in_memory_search(query_embedding.vector, top_k, filters)

    def _build_filter(self, filters: dict[str, Any]) -> Any:
        """Build Qdrant filter from dictionary."""
        if not filters or self._models is None:
            return None

        conditions = []

        for key, value in filters.items():
            if value is None:
                continue

            if key == "date_range" and isinstance(value, dict):
                # Handle date range filter
                if "start" in value:
                    conditions.append(
                        self._models.FieldCondition(
                            key="date",
                            range=self._models.Range(gte=value["start"]),
                        )
                    )
                if "end" in value:
                    conditions.append(
                        self._models.FieldCondition(
                            key="date",
                            range=self._models.Range(lte=value["end"]),
                        )
                    )
            elif isinstance(value, list):
                # Match any value in list
                conditions.append(
                    self._models.FieldCondition(
                        key=key,
                        match=self._models.MatchAny(any=value),
                    )
                )
            else:
                # Exact match
                conditions.append(
                    self._models.FieldCondition(
                        key=key,
                        match=self._models.MatchValue(value=value),
                    )
                )

        if not conditions:
            return None

        return self._models.Filter(must=conditions)

    def _in_memory_search(
        self,
        query_vector,
        top_k: int,
        filters: Optional[dict[str, Any]],
    ) -> list[SearchResult]:
        """Fallback in-memory search."""
        import numpy as np

        results = []

        for chunk_id, chunk in self._in_memory_store.items():
            # Apply filters
            if filters:
                match = True
                for key, value in filters.items():
                    if key in chunk.metadata:
                        if isinstance(value, list):
                            if chunk.metadata[key] not in value:
                                match = False
                                break
                        elif chunk.metadata[key] != value:
                            match = False
                            break
                if not match:
                    continue

            # Calculate similarity
            if chunk.embedding:
                chunk_vector = np.array(chunk.embedding)
                similarity = np.dot(query_vector, chunk_vector) / (
                    np.linalg.norm(query_vector) * np.linalg.norm(chunk_vector)
                )
            else:
                similarity = 0.0

            results.append(
                SearchResult(
                    chunk_id=chunk_id,
                    document_id=chunk.document_id,
                    content=chunk.content,
                    score=float(similarity),
                    metadata=chunk.metadata,
                    document_metadata=None,
                )
            )

        # Sort by score and return top_k
        results.sort(key=lambda x: x.score, reverse=True)
        return results[:top_k]


    def delete_document(self, document_id: str) -> bool:
        """
        Remove a document and all its chunks from the index.

        Args:
            document_id: ID of the document to delete

        Returns:
            True if deletion was successful
        """
        if self._client is None:
            # In-memory deletion
            to_delete = [
                cid for cid, chunk in self._in_memory_store.items()
                if chunk.document_id == document_id
            ]
            for cid in to_delete:
                del self._in_memory_store[cid]
            return len(to_delete) > 0

        try:
            self._client.delete(
                collection_name=self.collection_name,
                points_selector=self._models.FilterSelector(
                    filter=self._models.Filter(
                        must=[
                            self._models.FieldCondition(
                                key="document_id",
                                match=self._models.MatchValue(value=document_id),
                            )
                        ]
                    )
                ),
            )
            return True
        except Exception:
            return False

    def get_document_metadata(self, document_id: str) -> Optional[dict[str, Any]]:
        """
        Retrieve metadata for a specific document.

        Args:
            document_id: Document ID

        Returns:
            Document metadata or None if not found
        """
        # Search for any chunk from this document
        results = self.search(
            query="",
            top_k=1,
            filters={"document_id": document_id},
        )

        if results:
            return results[0].metadata
        return None

    def list_documents(
        self,
        filters: Optional[dict[str, Any]] = None,
        limit: int = 100,
    ) -> list[dict[str, Any]]:
        """
        List indexed documents with optional filtering.

        Args:
            filters: Optional metadata filters
            limit: Maximum number of documents to return

        Returns:
            List of document metadata dictionaries
        """
        if self._client is None:
            # In-memory listing
            seen_docs = {}
            for chunk in self._in_memory_store.values():
                doc_id = chunk.document_id
                if doc_id not in seen_docs:
                    seen_docs[doc_id] = chunk.metadata
            return list(seen_docs.values())[:limit]

        try:
            # Scroll through collection to get unique documents
            qdrant_filter = self._build_filter(filters) if filters else None

            results, _ = self._client.scroll(
                collection_name=self.collection_name,
                scroll_filter=qdrant_filter,
                limit=limit * 10,  # Get more to account for multiple chunks per doc
                with_payload=True,
                with_vectors=False,
            )

            # Deduplicate by document_id
            seen_docs = {}
            for point in results:
                doc_id = point.payload.get("document_id")
                if doc_id and doc_id not in seen_docs:
                    seen_docs[doc_id] = {
                        k: v for k, v in point.payload.items()
                        if k != "content"
                    }

            return list(seen_docs.values())[:limit]

        except Exception:
            return []

    def get_collection_stats(self) -> dict[str, Any]:
        """Get statistics about the knowledge base collection."""
        if self._client is None:
            return {
                "total_chunks": len(self._in_memory_store),
                "total_documents": len(set(
                    c.document_id for c in self._in_memory_store.values()
                )),
                "storage": "in-memory",
            }

        try:
            info = self._client.get_collection(self.collection_name)
            return {
                "total_chunks": info.points_count,
                "vectors_count": info.vectors_count,
                "status": info.status.value,
                "storage": "qdrant",
            }
        except Exception:
            return {"error": "Could not retrieve collection stats"}
