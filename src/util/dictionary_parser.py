import os
from src.ui.model import Button
from typing import Dict, List, Tuple


class Dictionary:
  table: Dict[Tuple[Button], str] = dict()

  def __init__(self):
    pass

  def add_word(self, string, buttons: List[Button]):
    if len(buttons) == 0:
      raise ValueError("Cannot create a dictionary entry for 0 buttons")

    key = tuple(buttons)
    if key in self.table:
      raise ValueError("The key `{}` is already in the table".format(buttons))
    self.table[key] = string

  def get_word(self, buttons: List[Button]):
    key = tuple(buttons)
    word = ""
    if key in self.table:
      word = self.table[key]

    if word == "<space>":
      word = " "
    if word == "<newline>":
      word = "\n"

    return word

class DictionaryParser:

  def __init__(self, path: str):
    self.path = os.path.abspath(path)

  def parse(self):
    # check if path exists
    dictionary = Dictionary()
    with open(self.path, "r") as dictionary_file:
      # get lines of path
      lines = dictionary_file.readlines()

      for line in lines:
        no_whitespace = "".join(line.split())
        tokens = no_whitespace.split("=")
        if len(tokens) != 2:
          raise ValueError("Invalid line `{}` in dictionary file".format(line))
        word = tokens[0]
        buttons = tokens[1]
        buttons_list = [DictionaryParser.button_value(b) for b in buttons.split(",")]
        dictionary.add_word(word, buttons_list)

    return dictionary

  @staticmethod
  def button_value(button: str):
    if len(button) != 1:
      raise ValueError("Invalid button `{}` in dictionary file".format(button))

    button = button.upper()

    if button == 'G':
      return Button.GREEN
    if button == 'R':
      return Button.RED
    if button == 'Y':
      return Button.YELLOW
    if button == 'B':
      return Button.BLUE
    if button == 'O':
      return Button.ORANGE
    raise ValueError("Invalid button `{}` in dictionary file".format(button))