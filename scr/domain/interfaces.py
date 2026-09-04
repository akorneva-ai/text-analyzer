from typing import Protocol

from .types import Language, Polarity


class Syllable_Counter(Protocol):
    def __call__(self, word: str) -> int: ...


class Language_Detector(Protocol):
    def __call__(self, text: str) -> Language: ...


class Sentiment_Analyzer(Protocol):
    def __call__(self, text: str) -> tuple[Polarity, float]: ...
