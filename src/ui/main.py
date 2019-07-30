from PyQt5.QtWidgets import QWidget

from src.util import dpi


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(dpi.dp(500), dpi.dp(500))
        self.move(dpi.dp(300), dpi.dp(300))
        self.setWindowTitle("GH Typer")
