from PyQt5.QtWidgets import QApplication
from PyQt5.Qt import QTimer
import time
from src.ui.model import JoystickState, ViewModel
from typing import Callable, TypeVar

T = TypeVar("T")


class JoystickDebouncer:
  def __init__(self, window: QApplication, poll_rate_hertz: float, debounce_millis: float):
    self.window = window
    self.poll_rate_hertz = poll_rate_hertz
    self.debounce_millis = debounce_millis

    # Receive input here
    self.trigger = None
    self.triggered = False  # https://imgur.com/gallery/TYSBw
    self.trigger_last_value = JoystickState()
    self.trigger_collector = ViewModel()
    self.trigger_last_called = JoystickDebouncer.now_millis()
    # Call this function when debounced output is ready
    self.notify: Callable[[T], None] = lambda x: None

    self.timer = QTimer(self.window)

  @staticmethod
  def now_millis():
    return int(round(time.time() * 1000))

  def start(self):
    """
    Call this function to begin debouncing from `self.trigger`.
    """
    self.timer.timeout.connect(self.refresh)
    self.timer.start(1000 / self.poll_rate_hertz)

  def refresh(self):
    # decide whether or not to call `out`
    now: int = JoystickDebouncer.now_millis()
    new_trigger_value = self.trigger()

    if new_trigger_value != self.trigger_last_value:
      self.trigger_last_called = now
      self.trigger_last_value = new_trigger_value
      self.trigger_collector.merge(new_trigger_value)
      self.triggered = True

    if now - self.trigger_last_called > self.debounce_millis and self.triggered:
      self.triggered = False
      self.trigger_last_called = now
      self.notify(self.trigger_collector)
      self.trigger_collector.clear()


