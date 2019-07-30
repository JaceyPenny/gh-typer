from PyQt5.QtWidgets import QWidget, QLabel

from src.util import dpi
from src.ui.model import ViewModel

dp = dpi.dp


def pressed_text(color, value):
    if value:
        return "{} PRESSED".format(color)
    else:
        return "{} NOT PRESSED".format(color)


class MainWindow(QWidget):
    view_model: ViewModel = None
    green_label = None
    red_label = None
    yellow_label = None
    blue_label = None
    orange_label = None

    def __init__(self, view_model: ViewModel):
        super().__init__()
        self.view_model = view_model
        self.resize(dp(500), dp(500))
        self.move(dp(300), dp(300))
        self.setWindowTitle("GH Typer")
        self.layout()

    def layout(self):
        self.green_label = QLabel(self)
        self.red_label = QLabel(self)
        self.yellow_label = QLabel(self)
        self.blue_label = QLabel(self)
        self.orange_label = QLabel(self)

        self.green_label.move(dp(24), dp(24))
        self.red_label.move(dp(24), dp(48))
        self.yellow_label.move(dp(24), dp(72))
        self.blue_label.move(dp(24), dp(96))
        self.orange_label.move(dp(24), dp(120))

        self.green_label.setText("Green NOT pressed")
        self.red_label.setText("Red NOT pressed")
        self.yellow_label.setText("Yellow NOT pressed")
        self.blue_label.setText("Blue NOT pressed")
        self.orange_label.setText("Orange NOT pressed")

    def update(self):
        self.green_label.setText(pressed_text("green", self.view_model.green_pressed))
        self.red_label.setText(pressed_text("red", self.view_model.red_pressed))
        self.yellow_label.setText(pressed_text("yellow", self.view_model.yellow_pressed))
        self.blue_label.setText(pressed_text("blue", self.view_model.blue_pressed))
        self.orange_label.setText(pressed_text("orange", self.view_model.orange_pressed))
