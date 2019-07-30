import sys
import src.util.dpi as dpi
import src.xbox as xbox
from PyQt5.QtWidgets import QApplication, QWidget


class Application:
    def __init__(self):
        self.app = None
        self.window = None
        self.joystick = None

    def start(self):
        if self.app is not None:
            return

        self.app = QApplication(sys.argv)
        dpi.DPI = self.app.screens()[0].physicalDotsPerInch()

        self.init_window()

        self.joystick = xbox.Joystick()
        self.app.exec_()

    def init_window(self):
        self.window = QWidget()
        self.window.resize(dpi.dp(500), dpi.dp(500))
        self.window.move(dpi.dp(300), dpi.dp(300))
        self.window.setWindowTitle("GH Typer")
        self.window.show()
