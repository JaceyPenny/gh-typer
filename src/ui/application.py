import sys
import src.xbox as xbox
from src.ui.main import *
from PyQt5.QtWidgets import QApplication


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
        self.window = MainWindow()
        self.window.show()
