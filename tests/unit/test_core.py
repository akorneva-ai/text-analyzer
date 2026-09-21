import pytest
from scr.domain.types import Language, Polarity
from scr.infrastructure.syllable_counters import Syllable_Counter
from scr.infrastructure.language_detector import Language_Detector
from scr.infrastructure.sentiment import Sentiment_Analyzer


def test_syllable_counter():
    counter = Syllable_Counter()
    # Проверяем русский язык через Enum
    assert counter.count("программа", Language.RU) == 3
    # Проверяем английский язык
    assert counter.count("python", Language.EN) == 2
    # Слово без гласных возвращает минимум 1
    assert counter.count("вспс", Language.RU) == 1


def test_language_detector_letters():
    detector = Language_Detector()
    # Кириллица возвращает Language.RU
    assert detector.detect("Привет") == Language.RU
    # Французские символы
    assert detector.detect("génial") == Language.FR
    # Немецкие умлауты
    assert detector.detect("schön") == Language.GER


def test_language_detector_words():
    detector = Language_Detector()
    # Проверка работы по словарям
    assert detector.detectByWords("the and of") == Language.EN
    assert detector.detectByWords("der die das") == Language.GER
    assert detector.detectByWords("le la les") == Language.FR


def test_sentiment_analyzer():
    analyzer = Sentiment_Analyzer()
    # Английский позитивный текст
    polarity, mood = analyzer.analyze("love happy nice", Language.EN)
    assert polarity == 1.0
    assert mood == Polarity.POSITIVE

    # Русский негативный текст
    polarity_ru, mood_ru = analyzer.analyze("ненавижу ужасный плохой", Language.RU)
    assert polarity_ru == -1.0
    assert mood_ru == Polarity.NEGATIVE
