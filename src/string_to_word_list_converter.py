import re

class StringToWordListConverter:
  def __init__(self, text):
    self.text = text

  def convert(self):
    return re.findall(r"[\w']+|[\".,!?;:()]", self.text)
