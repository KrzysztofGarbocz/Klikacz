from pynput.mouse import Button
from pynput.keyboard import Key
from Controller import Controller

class Process:
    def __init__(self):
        self.controller = Controller('action.json')

    def start(self):
        mapper = {
            {'Click_button': lambda value: self.controller.clik_button(getattr(Key, value))},
            {'Type': self.controller.type},
            {'Click_button':  lambda value: self.controller.clik_button(getattr(Key, value))},
            {'Hold_and_press': lambda  value: self.controller.hold_and_press(getattr(Key, value))},
            {'Mouse_clik': self.controller.mouse_clik}
            }
        for step in self.controller.steps:
            for key, value in step.items():
                mapper[key](**value)
