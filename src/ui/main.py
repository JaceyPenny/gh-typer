from PyQt5.QtWidgets import QWidget, QLabel, QListWidget

from src.util import dpi
from src.ui.model import ViewModel

dp = dpi.dp


class MainWindow(QWidget):
  app = None
  list_widget = None

  def __init__(self, app):
    super().__init__()
    self.app = app
    self.resize(dp(500), dp(500))
    self.move(dp(300), dp(300))
    self.setWindowTitle("GH Typer")
    self.layout()

  def layout(self):
    self.list_widget = QListWidget(self)
    self.list_widget.move(dp(24), dp(24))
    self.list_widget.resize(dp(400), dp(400))
    self.list_widget.show()

  def view_model(self) -> ViewModel:
    return self.app.view_model

  def update(self):
    view_model = self.view_model()
    self.list_widget.clear()
    for button in view_model.series:
      self.list_widget.addItem(repr(button))
