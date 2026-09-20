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

    return {
      'language': language,
      'sentences': sentences,
      'words': words,
      'syllables': syllables,
      'avgSentence': avgSentence,
      'avgWord': avgWord,
      'score': score,
      'meaning': meaning,
      'polarity': polarity,
      'mood': mood,
      'objectivity': objectivity
    }