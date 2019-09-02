from enum import Enum
from typing import List, Optional


class JoystickState:
  def __init__(self):
    self.green_pressed = False
    self.red_pressed = False
    self.yellow_pressed = False
    self.blue_pressed = False
    self.orange_pressed = False
    self.strummed_down = False
    self.strummed_up = False

  def __eq__(self, other: "ViewModel"):
    if other is None:
      return False

    return self.green_pressed == other.green_pressed \
        and self.red_pressed == other.red_pressed \
        and self.yellow_pressed == other.yellow_pressed \
        and self.blue_pressed == other.blue_pressed \
        and self.orange_pressed == other.orange_pressed \
        and self.strummed_down == other.strummed_down \
        and self.strummed_up == other.strummed_up

  def __repr__(self):
    return "G: {}, R: {}, Y: {}, B: {}, O: {}, SD: {}, SU: {}".format(
      self.state("green_pressed"),
      self.state("red_pressed"),
      self.state("yellow_pressed"),
      self.state("blue_pressed"),
      self.state("orange_pressed"),
      self.state("strummed_down"),
      self.state("strummed_up")
    )

  def state(self, variable: str):
    return "on" if getattr(self, variable) is True else "off"


class Button(Enum):
  GREEN = 1
  RED = 2
  YELLOW = 3
  BLUE = 4
  ORANGE = 5
  STRUM_UP = 6
  STRUM_DOWN = 7


class ViewModel:
  series: List[Button] = []

  def __init__(self):
    pass

  def merge(self, joystick_state: JoystickState):
    last_button: Button = ViewModel.get_last_button(joystick_state)
    if last_button is not None:
      if not self.series:
        self.series.append(last_button)
      elif last_button != self.series[-1]:
        self.series.append(last_button)

  @staticmethod
  def get_last_button(joystick_state: JoystickState) -> Optional[Button]:
    if joystick_state.orange_pressed:
      return Button.ORANGE
    if joystick_state.blue_pressed:
      return Button.BLUE
    if joystick_state.yellow_pressed:
      return Button.YELLOW
    if joystick_state.red_pressed:
      return Button.RED
    if joystick_state.green_pressed:
      return Button.GREEN
    return None

  def clear(self):
    self.series.clear()
