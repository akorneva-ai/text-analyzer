class Sentiment_Analyzer:

  def analyze(self, text, language):
    text = text.lower()
    words = text.split()

    if language == 'RU':
      good = [ru.GOOD, ru.EXCELLENT, ru.BEAUTIFUL, ru.WONDERFUL, ru.LOVE, ru.LIKE]
      bad = [ru.BAD, ru.TERRIBLE, ru.DISGUSTING, ru.HATE, ru.NOT_LIKE]
    elif language == 'FR':
      good = ['bon', 'excellent', 'super', 'génial', 'merveilleux', 'heureux', 'beau']
      bad = ['mauvais', 'terrible', 'horrible', 'triste', 'affreux', 'problème']
    elif language == 'DER':
      good = ['gut', 'exzellent', 'super', 'toll', 'wunderbar', 'schön', 'glücklich']
      bad = ['schlecht', 'schrecklich', 'traurig', 'böse', 'problem', 'furchtbar']
    else:
      good = ['good', 'great', 'excellent', 'wonderful', 'love', 'happy', 'nice']
      bad = ['bad', 'terrible', 'awful', 'hate', 'sad', 'problem', 'ugly']

    plus = 0
    minus = 0
    for word in words:
      if word in good:
        plus = plus + 1
      if word in bad:
        minus = minus + 1

    total = plus + minus
    if total == 0:
      polarity = 0
    else:
      polarity = (plus - minus) / total

    if polarity <= -0.33:
      mood = 'негативный'
    elif polarity >= 0.33:
      mood = 'позитивный'
    else:
      mood = 'нейтральный'

    return polarity, mood