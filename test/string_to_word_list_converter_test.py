import unittest
from src.string_to_word_list_converter import StringToWordListConverter

class StringToWordListConverterTest(unittest.TestCase):
  def string_to_list(self, text):
    return StringToWordListConverter(text).convert()

  def test_turns_string_into_list(self):
    text = "This is a simple string"
    self.assertEqual(self.string_to_list(text), ["This", "is", "a", "simple", "string"])

  def test_extracts_commas(self):
    text = "This, is a simple, string"
    self.assertEqual(self.string_to_list(text), ["This", ",", "is", "a", "simple", ",", "string"])

  def test_extracts_semicolons(self):
    text = "This; is a simple; string"
    self.assertEqual(self.string_to_list(text), ["This", ";", "is", "a", "simple", ";", "string"])

  def test_extracts_double_quotes(self):
    text = 'This "is" yours'
    self.assertEqual(self.string_to_list(text), ['This', '"', 'is', '"', 'yours'])

  def test_doesnt_extract_single_quotes(self):
    text = "This is your's and not our's"
    self.assertEqual(self.string_to_list(text), ["This", "is", "your's", "and", "not", "our's"])

  def test_emoji_characters(self):
    text = "This is :) and :p"
    self.assertEqual(self.string_to_list(text), ["This", "is", ":", ")", "and", ":", "p"])
