import json
from time import sleep
from pynput import mouse, keyboard
from pynput.mouse import Button


def wait(fun):
    """Decorator to wait 1.5s"""
    def wrapper(*args, **kwargs):
        sleep(1.5)
        return fun(*args, **kwargs)

    return wrapper


class Controller:
    def __init__(self, app_name):
        self.mouse = mouse.Controller()
        self.keyboard = keyboard.Controller()
        self.json_name = app_name
        self.steps = []
        self.load_steps()

    @wait
    def clik_button(self, key):
        with self.keyboard.pressed(key):
            pass

    @wait
    def press_button(self, key):
        self.keyboard.press(key)

    @wait
    def release(self, key):
        self.keyboard.release(key)

    @wait
    def hold_and_press(self, key_hold, key_press):
        with self.keyboard.pressed(key_hold):
            self.keyboard.press(key_press)

    def load_steps(self):
        with open(self.json_name, 'r', encoding='UTF-8') as file:
            self.steps = json.load(file)['STEPS']

    @wait
    def type(self, text):
        self.keyboard.type(text)
    @wait
    def draw_line(self, x, y, dx, button=Button.left):
        self.mouse.position = (x, y)
        self.mouse.press(button)
        for _ in range(0, int(dx)):
            self.mouse.move(1, 0)
            sleep(0.01)
        self.mouse.release(button)
    @wait
    def mouse_clik(self, x_coord, y_coord, button=Button.left):
        self.mouse.position = (x_coord, y_coord)
        self.mouse.click(button, 1)
