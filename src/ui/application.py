import sys
import src.xbox as xbox
from src.ui.main import *
from PyQt5.QtWidgets import QApplication
from PyQt5.Qt import QTimer


class Application:
    app: QApplication = None
    window: MainWindow = None
    joystick: xbox.Joystick = None
    timer: QTimer = None

    def __init__(self):
        self.refresh_rate = 30
        self.view_model = ViewModel()

    def start(self):
        if self.app is not None:
            return

        self.app = QApplication(sys.argv)
        dpi.DPI = self.app.screens()[0].physicalDotsPerInch()

        self.init_window()
        self.joystick = xbox.Joystick(self.refresh_rate)

        # Init timer
        self.timer = QTimer(self.window)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000 / self.refresh_rate)

        sys.exit(self.app.exec_())

    def update(self):
        self.update_view_model()
        self.window.update()

    def update_view_model(self):
        self.view_model.green_pressed = self.joystick.A() == 1
        self.view_model.red_pressed = self.joystick.B() == 1
        self.view_model.yellow_pressed = self.joystick.Y() == 1
        self.view_model.blue_pressed = self.joystick.X() == 1
        self.view_model.orange_pressed = self.joystick.leftBumper() == 1

    def init_window(self):
        self.window = MainWindow(self.view_model)
        self.window.show()
