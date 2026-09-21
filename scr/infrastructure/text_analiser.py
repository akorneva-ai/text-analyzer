from textblob import TextBlob
from domain.types import Analysis_Result, Text_Stats, Language

from infrastructure.language_detector import Language_Detector
from infrastructure.syllable_counters import Syllable_Counter
from infrastructure.flesch_calculators import Flesch_Calculator
from infrastructure.sentiment import Sentiment_Analyzer

class Text_Analyzer:

  def __init__(self):
    self.lang = Language_Detector()
    self.syll = Syllable_Counter()
    self.flesch = Flesch_Calculator()
    self.mood = Sentiment_Analyzer()

  def analyze(self, text):
    language = self.lang.detect(text)

    blob = TextBlob(text)
    sentences = len(blob.sentences)
    words = len(blob.words)

    syllables = 0
    for word in blob.words:
      syllables = syllables + self.syll.count(str(word), language)

    avgSentence = words / sentences
    avgWord = syllables / words

    score = self.flesch.calculate(sentences, words, syllables, language)
    meaning = self.flesch.interpret(score, language)

    polarity, mood = self.mood.analyze(text, language)
    objectivity = 100 - abs(polarity * 100)

    return Analysis_Result(
      language = language,
      flesch_index = score,
      interpretation = meaning,
      polarity = polarity,
      subjectivity = objectivity,
      stats = Text_Stats(
        sentence_count = sentences,
        word_count = words,
        syllable_count = syllables,
        avg_sentence_length = avgSentence,
        avg_word_syllables = avgWord
      )
    )