import unittest
from src.example import Example

class TestExample(unittest.TestCase):
  def test_it_works(self):
    self.assertEqual(Example(1).x, 1)
