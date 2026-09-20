class Flesch_Calculator:

  def calculate(self, sentences, words, syllables, language):
    s = words / sentences
    w = syllables / words

    if language == 'RU':
      return 206.835 - (1.52 * s) - (65.14 * w)
    else:
      return 206.835 - (1.015 * s) - (84.6 * w)

  def interpret(self, score, language):
    if language == 'RU':
      if score >= 80:
        return ru.EASY
      elif score >= 70:
        return ru.PRETTY_EASY
      elif score >= 60:
        return ru.ORDINARY
      elif score >= 50:
        return ru.QUITE_DIFFICULT
      elif score >= 30:
        return ru.DIFFICULT
      else:
        return ru.VERY_DIFFICULT
    else:
      if score >= 90:
        return ru.VERY_EASY
      elif score >= 80:
        return ru.EASY
      elif score >= 70:
        return ru.PRETTY_EASY
      elif score >= 60:
        return ru.ORDINARY
      elif score >= 50:
        return ru.QUITE_DIFFICULT
      elif score >= 30:
        return ru.DIFFICULT
      else:
        return ru.VERY_DIFFICULT