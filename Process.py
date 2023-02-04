from pynput.keyboard import Key
from Controller import Controller


class Process:
    def __init__(self, action_name: str):
        self.controller = Controller(action_name)
        self.mapper = {}

    def start(self):
        self.mapper = {
            'Click_button': lambda key: self.controller.clik_button(getattr(Key, key)),
            'Type': self.controller.type,
            'Hold_and_press': lambda key_hold, key_press: self.controller.hold_and_press
            (getattr(Key, key_hold), getattr(Key, key_press)),
            'Mouse_clik': self.controller.mouse_clik,
            'Mouse_draw': self.controller.draw_line
            }
        for step in self.controller.steps:
            for key, value in step.items():
                print(f'Key: {key}, Value: {value}')
                self.mapper[key](**value)
