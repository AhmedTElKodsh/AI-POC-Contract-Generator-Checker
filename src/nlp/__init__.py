"""NLP Processing Module for Arabic and English text."""

from src.nlp.processor import NLPProcessor
from src.nlp.embeddings import EmbeddingGenerator
from src.nlp.arabic_processor import ArabicProcessor

__all__ = [
    "NLPProcessor",
    "EmbeddingGenerator",
    "ArabicProcessor",
]
