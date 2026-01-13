"""Main NLP Processor module."""

import re
from typing import Optional

from src.ingestion.language_detector import LanguageDetector
from src.models.enums import Language
from src.nlp.arabic_processor import (
    ARABIC_ENGINEERING_TERMS,
    ArabicProcessor,
    TokenizedText,
)
from src.nlp.embeddings import EmbeddingGenerator, EmbeddingResult


# English engineering terms dictionary
ENGLISH_ENGINEERING_TERMS = {
    # Hydraulic Engineering
    "hydrological": "hydrology",
    "hydraulic": "hydraulics",
    "discharge": "flow",
    "flood": "flooding",
    "catchment": "watershed",
    "drainage": "drainage system",
    "stormwater": "storm drainage",
    "groundwater": "subsurface water",
    "runoff": "surface runoff",
    "infiltration": "water infiltration",
    # Structural Engineering
    "structural": "structures",
    "concrete": "cement concrete",
    "reinforcement": "steel reinforcement",
    "foundation": "building foundation",
    "bridge": "bridge structure",
    "beam": "structural beam",
    "column": "structural column",
    # Geotechnical
    "geotechnical": "soil mechanics",
    "soil": "earth material",
    "borehole": "soil boring",
    "bearing capacity": "load capacity",
    "settlement": "ground settlement",
    # General
    "project": "engineering project",
    "study": "technical study",
    "design": "engineering design",
    "specification": "technical specification",
    "boq": "bill of quantities",
    "proposal": "technical proposal",
}


class NLPProcessor:
    """
    Main NLP processor for Arabic and English text.

    Provides:
    - Tokenization for both languages
    - Morphological analysis for Arabic
    - Embedding generation
    - Technical term detection
    - Language detection and segmentation
    """

    def __init__(
        self,
        arabic_model: Optional[str] = None,
        english_model: Optional[str] = None,
        use_gpu: bool = False,
    ):
        """
        Initialize the NLP processor.

        Args:
            arabic_model: HuggingFace model ID for Arabic
            english_model: Model ID for English embeddings
            use_gpu: Whether to use GPU acceleration
        """
        self.arabic_processor = ArabicProcessor()
        self.embedding_generator = EmbeddingGenerator(
            arabic_model=arabic_model,
            english_model=english_model,
            use_gpu=use_gpu,
        )
        self.language_detector = LanguageDetector()

    def tokenize_arabic(self, text: str) -> TokenizedText:
        """
        Tokenize Arabic text with morphological analysis.

        Args:
            text: Arabic text to tokenize

        Returns:
            TokenizedText with tokens, lemmas, and POS tags
        """
        return self.arabic_processor.tokenize(text)

    def tokenize_english(self, text: str) -> TokenizedText:
        """
        Tokenize English text.

        Args:
            text: English text to tokenize

        Returns:
            TokenizedText with tokens
        """
        # Simple whitespace tokenization with punctuation handling
        tokens = re.findall(r"\b\w+\b", text.lower())

        return TokenizedText(
            tokens=tokens,
            lemmas=tokens,  # No lemmatization for now
            pos_tags=["UNK"] * len(tokens),
            language=Language.ENGLISH,
            original_text=text,
        )

    def tokenize(self, text: str) -> TokenizedText:
        """
        Tokenize text, auto-detecting language.

        Args:
            text: Text to tokenize

        Returns:
            TokenizedText with appropriate processing
        """
        language = self.language_detector.detect(text)

        if language == Language.ARABIC:
            return self.tokenize_arabic(text)
        elif language == Language.ENGLISH:
            return self.tokenize_english(text)
        else:
            # Mixed - tokenize as Arabic (handles both)
            return self.tokenize_arabic(text)

    def generate_embedding(self, text: str, language: Optional[Language] = None) -> EmbeddingResult:
        """
        Generate vector embedding for text.

        Args:
            text: Text to embed
            language: Language (auto-detected if not provided)

        Returns:
            EmbeddingResult with vector and metadata
        """
        if language is None:
            language = self.language_detector.detect(text)

        return self.embedding_generator.generate(text, language)

    def normalize_arabic(self, text: str) -> str:
        """
        Normalize Arabic text to MSA.

        Args:
            text: Arabic text to normalize

        Returns:
            Normalized text
        """
        return self.arabic_processor.normalize(text)


    def detect_technical_terms(self, text: str) -> list[tuple[str, str]]:
        """
        Identify engineering technical terms in text.

        Args:
            text: Text to analyze

        Returns:
            List of (term, category) tuples
        """
        found_terms = []
        text_lower = text.lower()

        # Check Arabic terms
        for arabic_term, english_equiv in ARABIC_ENGINEERING_TERMS.items():
            if arabic_term in text:
                found_terms.append((arabic_term, english_equiv))

        # Check English terms
        for english_term, category in ENGLISH_ENGINEERING_TERMS.items():
            if english_term in text_lower:
                found_terms.append((english_term, category))

        return found_terms

    def detect_language(self, text: str) -> Language:
        """
        Detect the primary language of text.

        Args:
            text: Text to analyze

        Returns:
            Language enum
        """
        return self.language_detector.detect(text)

    def detect_language_segments(self, text: str) -> list[tuple[str, Language]]:
        """
        Detect language of each segment in mixed text.

        Args:
            text: Text to analyze

        Returns:
            List of (segment, language) tuples
        """
        return self.language_detector.detect_segments(text)

    def preprocess_for_indexing(self, text: str) -> str:
        """
        Preprocess text for knowledge base indexing.

        Performs:
        - Language detection
        - Arabic normalization (if applicable)
        - Technical term preservation
        - Whitespace normalization

        Args:
            text: Text to preprocess

        Returns:
            Preprocessed text
        """
        if not text:
            return text

        language = self.detect_language(text)

        if language == Language.ARABIC:
            # Normalize Arabic text
            text = self.normalize_arabic(text)
        elif language == Language.MIXED:
            # Process Arabic segments only
            segments = self.detect_language_segments(text)
            processed_parts = []
            for segment, lang in segments:
                if lang == Language.ARABIC:
                    processed_parts.append(self.normalize_arabic(segment))
                else:
                    processed_parts.append(segment)
            text = " ".join(processed_parts)

        # Normalize whitespace
        text = re.sub(r"\s+", " ", text).strip()

        return text

    def chunk_text(
        self,
        text: str,
        chunk_size: int = 500,
        overlap: int = 50,
    ) -> list[str]:
        """
        Split text into chunks for indexing.

        Args:
            text: Text to chunk
            chunk_size: Target chunk size in characters
            overlap: Overlap between chunks

        Returns:
            List of text chunks
        """
        if not text or len(text) <= chunk_size:
            return [text] if text else []

        chunks = []
        start = 0

        while start < len(text):
            end = start + chunk_size

            # Try to break at sentence boundary
            if end < len(text):
                # Look for sentence endings
                for sep in [".", "。", "!", "?", "\n\n"]:
                    last_sep = text.rfind(sep, start, end)
                    if last_sep > start:
                        end = last_sep + 1
                        break

            chunk = text[start:end].strip()
            if chunk:
                chunks.append(chunk)

            start = end - overlap

        return chunks

    def extract_keywords(self, text: str, top_k: int = 10) -> list[str]:
        """
        Extract keywords from text.

        Args:
            text: Text to analyze
            top_k: Number of keywords to return

        Returns:
            List of keywords
        """
        # Tokenize
        tokenized = self.tokenize(text)

        # Count token frequencies
        from collections import Counter

        token_counts = Counter(tokenized.tokens)

        # Filter out common words (simple stopword removal)
        stopwords = {
            "the", "a", "an", "is", "are", "was", "were", "be", "been",
            "being", "have", "has", "had", "do", "does", "did", "will",
            "would", "could", "should", "may", "might", "must", "shall",
            "can", "of", "to", "in", "for", "on", "with", "at", "by",
            "from", "as", "into", "through", "during", "before", "after",
            "above", "below", "between", "under", "again", "further",
            "then", "once", "here", "there", "when", "where", "why",
            "how", "all", "each", "few", "more", "most", "other", "some",
            "such", "no", "nor", "not", "only", "own", "same", "so",
            "than", "too", "very", "just", "and", "but", "if", "or",
            "because", "until", "while", "this", "that", "these", "those",
            # Arabic stopwords
            "في", "من", "إلى", "على", "عن", "مع", "هذا", "هذه", "ذلك",
            "التي", "الذي", "التى", "الذى", "و", "أو", "ثم", "لكن",
        }

        keywords = [
            token for token, count in token_counts.most_common(top_k * 2)
            if token.lower() not in stopwords and len(token) > 2
        ]

        return keywords[:top_k]
