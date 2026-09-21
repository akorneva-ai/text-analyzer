import pytest
from unittest.mock import MagicMock, patch
from scr.infrastructure.syllable_counters import Syllable_Counter
from scr.infrastructure.language_detector import Language_Detector
from scr.infrastructure.sentiment import Sentiment_Analyzer
from scr.infrastructure.text_analiser import Text_Analyzer
from scr.infrastructure.flesch_calculators import Flesch_Calculator


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


def test_text_analyzer_integration():
    analyzer = Text_Analyzer()

    with patch("scr.infrastructure.text_analiser.TextBlob") as mock_blob:
        mock_instance = MagicMock()
        mock_instance.sentences = [MagicMock()]
        mock_instance.words = ["hello", "world"]
        mock_blob.return_value = mock_instance

        result = analyzer.analyze("hello world")

        assert result.stats.word_count == 2
        assert result.stats.sentence_count == 1


def test_flesch_calculator_math():
    calc = Flesch_Calculator()
    Language = type(Language_Detector().detect("test"))

    score_en = calc.calculate(sentences=1, words=10, syllables=15, language=Language.EN)
    assert round(score_en, 3) == 69.785
    score_ru = calc.calculate(sentences=1, words=10, syllables=15, language=Language.RU)
    assert round(score_ru, 3) == 93.925


def test_flesch_interpretation_all_branches():
    calc = Flesch_Calculator()
    Language = type(Language_Detector().detect("test"))

    assert "Легко читается" in calc.interpret(85, Language.RU)
    assert "Обычный" in calc.interpret(65, Language.RU)
    assert "Довольно трудно" in calc.interpret(55, Language.RU)
    assert "Трудно читается" in calc.interpret(35, Language.RU)
    assert "Очень трудно" in calc.interpret(10, Language.RU)

    assert "Очень легко" in calc.interpret(95, Language.EN)
    assert "Легко читается" in calc.interpret(85, Language.EN)
