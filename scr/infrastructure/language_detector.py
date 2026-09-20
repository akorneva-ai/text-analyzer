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
      return 'DER'
    elif frCount > derCount and frCount > enCount:
      return 'FR'
    else:
      return 'EN'

  def detect(self, text):
    for letter in text:
      if letter in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
        return 'RU'

    for letter in text:
      if letter in 'àâäéèêëïîôöùûüÿ':
        return 'FR'

    for letter in text:
      if letter in 'äöüß':
        return 'DER'

    try:
      lang = detect(text)
      if lang == 'ru':
        return 'RU'
      if lang == 'fr':
        return 'FR'
      if lang == 'de':
        return 'DER'
      return 'EN'
    except:
      return 'EN'