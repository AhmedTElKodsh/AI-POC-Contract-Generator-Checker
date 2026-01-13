"""Language detection for document content."""

import re
from typing import Optional

from src.models.enums import Language


class LanguageDetector:
    """Detect language of text content, with support for Arabic/English mixed text."""

    # Arabic Unicode range
    ARABIC_PATTERN = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]+")
    # Basic Latin (English) pattern
    ENGLISH_PATTERN = re.compile(r"[a-zA-Z]+")

    def __init__(self):
        """Initialize the language detector."""
        self._langdetect_available = False
        try:
            import langdetect

            self._langdetect = langdetect
            self._langdetect_available = True
        except ImportError:
            pass

    def detect(self, text: str) -> Language:
        """
        Detect the primary language of the text.

        Args:
            text: Text content to analyze

        Returns:
            Language enum indicating detected language
        """
        if not text or not text.strip():
            return Language.ENGLISH  # Default

        # Count Arabic and English characters
        arabic_chars = len(self.ARABIC_PATTERN.findall(text))
        english_chars = len(self.ENGLISH_PATTERN.findall(text))

        total_chars = arabic_chars + english_chars
        if total_chars == 0:
            return Language.ENGLISH

        arabic_ratio = arabic_chars / total_chars
        english_ratio = english_chars / total_chars

        # Determine language based on ratios
        if arabic_ratio > 0.7:
            return Language.ARABIC
        elif english_ratio > 0.7:
            return Language.ENGLISH
        elif arabic_ratio > 0.2 and english_ratio > 0.2:
            return Language.MIXED
        elif arabic_ratio > english_ratio:
            return Language.ARABIC
        else:
            return Language.ENGLISH

    def detect_with_langdetect(self, text: str) -> Optional[Language]:
        """
        Use langdetect library for more accurate detection.

        Args:
            text: Text content to analyze

        Returns:
            Language enum or None if detection fails
        """
        if not self._langdetect_available or not text.strip():
            return None

        try:
            detected = self._langdetect.detect(text)
            if detected == "ar":
                return Language.ARABIC
            elif detected == "en":
                return Language.ENGLISH
            else:
                # For other languages, fall back to character analysis
                return self.detect(text)
        except Exception:
            return None

    def detect_segments(self, text: str) -> list[tuple[str, Language]]:
        """
        Detect language of each segment in mixed-language text.

        Args:
            text: Text content to analyze

        Returns:
            List of (segment_text, language) tuples
        """
        if not text:
            return []

        segments = []
        current_segment = ""
        current_lang = None

        # Split by whitespace and analyze each word
        words = text.split()

        for word in words:
            word_lang = self._detect_word_language(word)

            if current_lang is None:
                current_lang = word_lang
                current_segment = word
            elif word_lang == current_lang or word_lang == Language.MIXED:
                current_segment += " " + word
            else:
                if current_segment:
                    segments.append((current_segment.strip(), current_lang))
                current_segment = word
                current_lang = word_lang

        # Add final segment
        if current_segment and current_lang:
            segments.append((current_segment.strip(), current_lang))

        return segments

    def _detect_word_language(self, word: str) -> Language:
        """Detect language of a single word."""
        has_arabic = bool(self.ARABIC_PATTERN.search(word))
        has_english = bool(self.ENGLISH_PATTERN.search(word))

        if has_arabic and has_english:
            return Language.MIXED
        elif has_arabic:
            return Language.ARABIC
        elif has_english:
            return Language.ENGLISH
        else:
            return Language.MIXED  # Numbers, symbols, etc.
