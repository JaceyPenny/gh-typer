import sys
import src.xbox as xbox
from src.ui.main import *
from src.ui.model import *
from src.util.debouncer import JoystickDebouncer
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
    self.debouncer: JoystickDebouncer = None

  def start(self):
    if self.app is not None:
      return

    self.app = QApplication(sys.argv)
    dpi.DPI = self.app.screens()[0].physicalDotsPerInch()

    self.init_window()
    self.joystick = xbox.Joystick(self.refresh_rate)

    # Init timer
    # TODO init debouncer
    self.debouncer = JoystickDebouncer(self.app, 60, 250)
    self.debouncer.trigger = self.get_joystick_state
    self.debouncer.notify = self.draw

    self.debouncer.start()

    sys.exit(self.app.exec_())

  def get_joystick_state(self) -> JoystickState:
    joystick_state = JoystickState()
    joystick_state.green_pressed = self.joystick.A() == 1
    joystick_state.red_pressed = self.joystick.B() == 1
    joystick_state.yellow_pressed = self.joystick.Y() == 1
    joystick_state.blue_pressed = self.joystick.X() == 1
    joystick_state.orange_pressed = self.joystick.leftBumper() == 1

    return joystick_state

  def draw(self, view_model: ViewModel):
    if view_model is None:
      return

    self.view_model = view_model
    self.window.update()

  def init_window(self):
    self.window = MainWindow(self)
    self.window.show()
