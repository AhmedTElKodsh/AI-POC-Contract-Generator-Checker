"""Embedding generation for Arabic and English text."""

from dataclasses import dataclass
from typing import Optional

import numpy as np

from src.models.enums import Language


@dataclass
class EmbeddingResult:
    """Vector embedding with metadata."""

    vector: np.ndarray
    text: str
    language: Language
    model_name: str
    dimension: int


class EmbeddingGenerator:
    """
    Generate embeddings for Arabic and English text.

    Uses AraBERT for Arabic text and sentence-transformers for English.
    Supports multilingual models for mixed content.
    """

    # Default models
    ARABIC_MODEL = "aubmindlab/bert-base-arabertv2"
    ENGLISH_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
    MULTILINGUAL_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

    def __init__(
        self,
        arabic_model: Optional[str] = None,
        english_model: Optional[str] = None,
        multilingual_model: Optional[str] = None,
        use_gpu: bool = False,
    ):
        """
        Initialize the embedding generator.

        Args:
            arabic_model: HuggingFace model ID for Arabic embeddings
            english_model: Model ID for English embeddings
            multilingual_model: Model ID for multilingual embeddings
            use_gpu: Whether to use GPU acceleration
        """
        self.arabic_model_name = arabic_model or self.ARABIC_MODEL
        self.english_model_name = english_model or self.ENGLISH_MODEL
        self.multilingual_model_name = multilingual_model or self.MULTILINGUAL_MODEL
        self.use_gpu = use_gpu

        self._sentence_transformer = None
        self._arabic_model = None
        self._arabic_tokenizer = None
        self._multilingual_model = None

        self._load_dependencies()

    def _load_dependencies(self):
        """Load embedding models."""
        # Try to load sentence-transformers
        try:
            from sentence_transformers import SentenceTransformer

            device = "cuda" if self.use_gpu else "cpu"
            self._sentence_transformer = SentenceTransformer(
                self.english_model_name, device=device
            )
        except ImportError:
            pass
        except Exception:
            pass

    def generate(self, text: str, language: Language) -> EmbeddingResult:
        """
        Generate embedding for text.

        Args:
            text: Text to embed
            language: Language of the text

        Returns:
            EmbeddingResult with vector and metadata
        """
        if not text.strip():
            # Return zero vector for empty text
            dim = 384  # Default dimension
            return EmbeddingResult(
                vector=np.zeros(dim),
                text=text,
                language=language,
                model_name="none",
                dimension=dim,
            )

        # Use appropriate model based on language
        if language == Language.ARABIC:
            return self._generate_arabic_embedding(text)
        elif language == Language.ENGLISH:
            return self._generate_english_embedding(text)
        else:
            # Mixed language - use multilingual model
            return self._generate_multilingual_embedding(text)

    def _generate_english_embedding(self, text: str) -> EmbeddingResult:
        """Generate embedding using sentence-transformers."""
        if self._sentence_transformer is None:
            return self._generate_fallback_embedding(text, Language.ENGLISH)

        try:
            vector = self._sentence_transformer.encode(text, convert_to_numpy=True)
            return EmbeddingResult(
                vector=vector,
                text=text,
                language=Language.ENGLISH,
                model_name=self.english_model_name,
                dimension=len(vector),
            )
        except Exception:
            return self._generate_fallback_embedding(text, Language.ENGLISH)

    def _generate_arabic_embedding(self, text: str) -> EmbeddingResult:
        """Generate embedding for Arabic text."""
        # Try to use AraBERT
        if self._arabic_model is None:
            try:
                from transformers import AutoModel, AutoTokenizer

                self._arabic_tokenizer = AutoTokenizer.from_pretrained(
                    self.arabic_model_name
                )
                self._arabic_model = AutoModel.from_pretrained(self.arabic_model_name)
            except Exception:
                # Fall back to multilingual
                return self._generate_multilingual_embedding(text)

        try:
            import torch

            inputs = self._arabic_tokenizer(
                text, return_tensors="pt", truncation=True, max_length=512
            )

            with torch.no_grad():
                outputs = self._arabic_model(**inputs)

            # Use CLS token embedding
            vector = outputs.last_hidden_state[:, 0, :].numpy().flatten()

            return EmbeddingResult(
                vector=vector,
                text=text,
                language=Language.ARABIC,
                model_name=self.arabic_model_name,
                dimension=len(vector),
            )
        except Exception:
            return self._generate_multilingual_embedding(text)


    def _generate_multilingual_embedding(self, text: str) -> EmbeddingResult:
        """Generate embedding using multilingual model."""
        if self._multilingual_model is None:
            try:
                from sentence_transformers import SentenceTransformer

                device = "cuda" if self.use_gpu else "cpu"
                self._multilingual_model = SentenceTransformer(
                    self.multilingual_model_name, device=device
                )
            except Exception:
                return self._generate_fallback_embedding(text, Language.MIXED)

        try:
            vector = self._multilingual_model.encode(text, convert_to_numpy=True)
            return EmbeddingResult(
                vector=vector,
                text=text,
                language=Language.MIXED,
                model_name=self.multilingual_model_name,
                dimension=len(vector),
            )
        except Exception:
            return self._generate_fallback_embedding(text, Language.MIXED)

    def _generate_fallback_embedding(
        self, text: str, language: Language
    ) -> EmbeddingResult:
        """Generate simple fallback embedding when models unavailable."""
        # Simple bag-of-words style embedding
        # This is a placeholder - in production, models should be available
        dim = 384
        np.random.seed(hash(text) % (2**32))
        vector = np.random.randn(dim).astype(np.float32)
        vector = vector / np.linalg.norm(vector)  # Normalize

        return EmbeddingResult(
            vector=vector,
            text=text,
            language=language,
            model_name="fallback",
            dimension=dim,
        )

    def batch_generate(
        self, texts: list[str], language: Language
    ) -> list[EmbeddingResult]:
        """
        Generate embeddings for multiple texts.

        Args:
            texts: List of texts to embed
            language: Language of the texts

        Returns:
            List of EmbeddingResult objects
        """
        results = []
        for text in texts:
            results.append(self.generate(text, language))
        return results

    def similarity(self, embedding1: EmbeddingResult, embedding2: EmbeddingResult) -> float:
        """
        Calculate cosine similarity between two embeddings.

        Args:
            embedding1: First embedding
            embedding2: Second embedding

        Returns:
            Cosine similarity score (0-1)
        """
        v1 = embedding1.vector
        v2 = embedding2.vector

        # Ensure same dimension
        if len(v1) != len(v2):
            return 0.0

        dot_product = np.dot(v1, v2)
        norm1 = np.linalg.norm(v1)
        norm2 = np.linalg.norm(v2)

        if norm1 == 0 or norm2 == 0:
            return 0.0

        return float(dot_product / (norm1 * norm2))
