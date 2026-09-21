import pytest
from scr.infrastructure.syllable_counters import Syllable_Counter
from scr.infrastructure.language_detector import Language_Detector
from scr.infrastructure.sentiment import Sentiment_Analyzer


def test_syllable_counter():
    counter = Syllable_Counter()
    Language = type(Language_Detector().detect("test"))

    assert counter.count("программа", Language.RU) == 3
    assert counter.count("python", Language.EN) == 2
    assert counter.count("вспс", Language.RU) == 1


def test_language_detector_letters():
    detector = Language_Detector()
    Language = type(detector.detect("test"))

    assert detector.detect("Привет") == Language.RU
    assert detector.detect("génial") == Language.FR
    assert detector.detect("schön") == Language.FR
    assert detector.detect("groß") == Language.GER


def test_language_detector_words():
    detector = Language_Detector()
    Language = type(detector.detect("test"))

    assert detector.detectByWords("the and of") == Language.EN
    assert detector.detectByWords("der die das") == Language.GER
    assert detector.detectByWords("le la les") == Language.FR


def test_sentiment_analyzer():
    analyzer = Sentiment_Analyzer()
    Language = type(Language_Detector().detect("test"))

    polarity, mood = analyzer.analyze("love happy nice", Language.EN)
    Polarity = type(mood)

    assert polarity == 1.0
    assert mood == Polarity.POSITIVE

    polarity_ru, mood_ru = analyzer.analyze("ненавижу ужасный плохой", Language.RU)
    assert polarity_ru == -1.0
    assert mood_ru == Polarity.NEGATIVE
