import unittest
from src.type_token_analyzer import TypeTokenAnalyzer

class TypeTokenAnalyzerTest(unittest.TestCase):
  def test_calculates_ratio_with_lowercase_words(self):
    words = ["hello", "i", "hello", "more", "i"]
    self.assertEqual(TypeTokenAnalyzer(words).ratio(), 3/5)

  def test_calculates_ratio_with_uppercase_words(self):
    words = ["hello", "I", "hello", "More", "i"]
    self.assertEqual(TypeTokenAnalyzer(words).ratio(), 3/5)
