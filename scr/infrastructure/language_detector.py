from langdetect import detect
from domain.types import Language

class Language_Detector:

  def detectByWords(self, text):
    words = text.lower().split()

    derWords = ['der', 'die', 'das', 'und', 'ich', 'du', 'wir', 'sie', 'er', 'es', 'nicht', 'ja', 'nein']
    frWords = ['le', 'la', 'les', 'un', 'une', 'je', 'tu', 'il', 'elle', 'nous', 'vous', 'ils', 'elles', 'oui', 'non']
    enWords = ['the', 'and', 'of', 'to', 'for', 'with', 'on', 'at', 'from', 'by', 'an', 'a', 'he', 'she', 'it']

    derCount = 0
    frCount = 0
    enCount = 0
    for word in words:
      if word in derWords:
        derCount = derCount + 1
      if word in frWords:
        frCount = frCount + 1
      if word in enWords:
        enCount = enCount + 1

    if derCount > frCount and derCount > enCount:
      return Language.GER
    elif frCount > derCount and frCount > enCount:
      return Language.FR
    else:
      return Language.EN

  def detect(self, text):
    for letter in text:
      if letter in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
        return Language.RU

    for letter in text:
      if letter in 'àâäéèêëïîôöùûüÿ':
        return Language.FR

    for letter in text:
      if letter in 'äöüß':
        return Language.GER

    try:
      lang = detect(text)
      if lang == 'ru':
        return Language.RU
      if lang == 'fr':
        return Language.FR
      if lang == 'de':
        return Language.GER
      return Language.EN
    except:
      return Language.EN