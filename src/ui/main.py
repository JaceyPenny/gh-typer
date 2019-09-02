from PyQt5.QtWidgets import QWidget, QLabel, QListWidget

from src.util import dpi
from src.util.dictionary_parser import Dictionary, DictionaryParser
from src.ui.model import ViewModel
from pprint import pprint


dp = dpi.dp


class MainWindow(QWidget):
  app = None
  list_widget: QListWidget = None
  text_label: QLabel = None

  def __init__(self, app):
    super().__init__()
    self.app = app
    self.resize(dp(500), dp(500))
    self.move(dp(300), dp(300))
    self.setWindowTitle("GH Typer")
    self.layout()
    self.dictionary: Dictionary = None

  def layout(self):
    self.list_widget = QListWidget(self)
    self.list_widget.move(dp(24), dp(24))
    self.list_widget.resize(dp(400), dp(300))
    self.list_widget.show()

    self.text_label = QLabel(self)
    self.text_label.move(dp(24), dp(348))
    self.text_label.resize(dp(400), dp(100))
    self.text_label.show()

  def load_dictionary(self):
    self.dictionary = DictionaryParser("./res/dictionary.txt").parse()

  def view_model(self) -> ViewModel:
    return self.app.view_model

  def update(self):
    view_model = self.view_model()
    self.list_widget.clear()
    for button in view_model.series:
      self.list_widget.addItem(repr(button))

    word = self.dictionary.get_word(view_model.series)
    if word == "<backspace>":
      view_model.current_text = view_model.current_text[:-1]
    else:
      view_model.current_text += word
    self.text_label.setText(view_model.current_text)
