from scr.domain.types import Language
class Syllable_Counter:

  def count(self, word, language):
    word = word.lower()
    if language == Language.RU:
      vowels = 'аеёиоуыэюя'
    elif language == Language.FR:
      vowels = 'aeiouyàâäéèêëïîôöùûüÿ'
    elif language == Language.GER:
      vowels = 'aeiouyäöüß'
    else:
      vowels = 'aeiouy'
    count = 0
    for letter in word:
      if letter in vowels:
        count = count + 1
    if count == 0:
      count = 1

    return count