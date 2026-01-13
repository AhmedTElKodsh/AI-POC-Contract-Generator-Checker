"""Arabic text processing using CAMeL Tools."""

import re
from dataclasses import dataclass
from typing import Optional

from src.models.enums import Language


@dataclass
class TokenizedText:
    """Tokenized text with morphological information."""

    tokens: list[str]
    lemmas: list[str]
    pos_tags: list[str]
    language: Language
    original_text: str


class ArabicProcessor:
    """
    Arabic NLP processor using CAMeL Tools.

    Provides tokenization, morphological analysis, and text normalization
    for Arabic text, including support for Modern Standard Arabic (MSA)
    and Egyptian Arabic dialect.
    """

    # Arabic diacritics (tashkeel)
    ARABIC_DIACRITICS = re.compile(r"[\u064B-\u065F\u0670]")

    # Arabic tatweel (kashida)
    ARABIC_TATWEEL = re.compile(r"\u0640")

    # Common Arabic character normalizations
    ALEF_VARIANTS = re.compile(r"[إأآا]")
    YEH_VARIANTS = re.compile(r"[يى]")
    TEH_MARBUTA = re.compile(r"ة")
    WAW_HAMZA = re.compile(r"ؤ")
    YEH_HAMZA = re.compile(r"ئ")

    def __init__(self):
        """Initialize the Arabic processor."""
        self._camel_tools_available = False
        self._analyzer = None
        self._tokenizer = None
        self._load_dependencies()

    def _load_dependencies(self):
        """Load CAMeL Tools if available."""
        try:
            from camel_tools.tokenizers.word import simple_word_tokenize
            from camel_tools.utils.normalize import normalize_unicode

            self._simple_tokenize = simple_word_tokenize
            self._normalize_unicode = normalize_unicode
            self._camel_tools_available = True

            # Try to load morphological analyzer (may require additional data)
            try:
                from camel_tools.morphology.analyzer import Analyzer

                self._analyzer = Analyzer.builtin_analyzer()
            except Exception:
                pass

        except ImportError:
            pass

    def tokenize(self, text: str) -> TokenizedText:
        """
        Tokenize Arabic text.

        Args:
            text: Arabic text to tokenize

        Returns:
            TokenizedText with tokens and morphological info
        """
        if not text.strip():
            return TokenizedText(
                tokens=[],
                lemmas=[],
                pos_tags=[],
                language=Language.ARABIC,
                original_text=text,
            )

        # Use CAMeL Tools if available
        if self._camel_tools_available:
            tokens = self._simple_tokenize(text)
        else:
            # Fallback to simple whitespace tokenization
            tokens = text.split()

        # Get lemmas and POS tags if analyzer is available
        lemmas = []
        pos_tags = []

        if self._analyzer:
            for token in tokens:
                analyses = self._analyzer.analyze(token)
                if analyses:
                    # Take first analysis
                    analysis = analyses[0]
                    lemmas.append(analysis.get("lex", token))
                    pos_tags.append(analysis.get("pos", "UNK"))
                else:
                    lemmas.append(token)
                    pos_tags.append("UNK")
        else:
            lemmas = tokens.copy()
            pos_tags = ["UNK"] * len(tokens)

        return TokenizedText(
            tokens=tokens,
            lemmas=lemmas,
            pos_tags=pos_tags,
            language=Language.ARABIC,
            original_text=text,
        )

    def normalize(self, text: str) -> str:
        """
        Normalize Arabic text to Modern Standard Arabic (MSA).

        Performs:
        - Unicode normalization
        - Diacritics removal
        - Character normalization (alef, yeh, etc.)
        - Tatweel removal

        Args:
            text: Arabic text to normalize

        Returns:
            Normalized text
        """
        if not text:
            return text

        # Unicode normalization
        if self._camel_tools_available:
            text = self._normalize_unicode(text)

        # Remove diacritics
        text = self.ARABIC_DIACRITICS.sub("", text)

        # Remove tatweel
        text = self.ARABIC_TATWEEL.sub("", text)

        # Normalize alef variants to bare alef
        text = self.ALEF_VARIANTS.sub("ا", text)

        # Normalize yeh variants
        text = self.YEH_VARIANTS.sub("ي", text)

        return text


    def remove_diacritics(self, text: str) -> str:
        """Remove Arabic diacritics (tashkeel) from text."""
        return self.ARABIC_DIACRITICS.sub("", text)

    def is_arabic(self, text: str) -> bool:
        """Check if text contains Arabic characters."""
        arabic_pattern = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]")
        return bool(arabic_pattern.search(text))

    def get_arabic_ratio(self, text: str) -> float:
        """Get ratio of Arabic characters in text."""
        if not text:
            return 0.0

        arabic_pattern = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]")
        arabic_chars = len(arabic_pattern.findall(text))
        total_chars = len(re.findall(r"\S", text))

        return arabic_chars / total_chars if total_chars > 0 else 0.0

    def extract_arabic_segments(self, text: str) -> list[str]:
        """Extract Arabic text segments from mixed text."""
        arabic_pattern = re.compile(
            r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\s]+"
        )
        segments = arabic_pattern.findall(text)
        return [s.strip() for s in segments if s.strip()]


# Engineering domain dictionary for Arabic technical terms
ARABIC_ENGINEERING_TERMS = {
    # Hydraulic Engineering
    "هيدرولوجي": "hydrological",
    "هيدروليكي": "hydraulic",
    "تصريف": "discharge",
    "فيضان": "flood",
    "حوض": "basin",
    "مستجمع": "catchment",
    "صرف": "drainage",
    "مياه أمطار": "stormwater",
    "مياه سطحية": "surface water",
    "مياه جوفية": "groundwater",
    # Structural Engineering
    "إنشائي": "structural",
    "خرسانة": "concrete",
    "حديد تسليح": "reinforcement",
    "أساسات": "foundations",
    "جسر": "bridge",
    "كوبري": "bridge",
    # Geotechnical
    "جيوتقني": "geotechnical",
    "تربة": "soil",
    "جسات": "boreholes",
    "تحمل": "bearing capacity",
    # General
    "مشروع": "project",
    "دراسة": "study",
    "تصميم": "design",
    "تنفيذ": "implementation",
    "مواصفات": "specifications",
    "جدول كميات": "bill of quantities",
    "عرض فني": "technical proposal",
    "عرض مالي": "financial proposal",
}
