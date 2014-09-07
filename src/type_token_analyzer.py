class TypeTokenAnalyzer:
  def __init__(self, words):
    self.words = words

  def ratio(self):
    return self._unique_word_count() / self._total_word_count()

  def _total_word_count(self):
    return len(self.words)

  def _unique_word_count(self):
    return len(set(self._words_to_lowercase()))

  def _words_to_lowercase(self):
    return list(map(lambda word: word.lower(), self.words))
