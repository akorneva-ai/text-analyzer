from dataclasses import dataclass
from enum import Enum, auto


class Language(Enum):
    EN = auto()
    RU = auto()
    GER = auto()
    FR = auto()


class Polarity(Enum):
    POSITIVE = "positive"
    NEGATIVE = "negative"
    NEUTRAL = "neutral"


@dataclass(frozen=True)
class Text_Stats:
    sentence_count: int
    word_count: int
    syllable_count: int
    avg_sentence_length: float
    avg_word_syllables: float


@dataclass(frozen=True)
class Analysis_Result:
    language: Language
    flesch_index: float
    interpretation: str
    polarity: Polarity
    subjectivity: float
    stats: Text_Stats
