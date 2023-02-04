import json
from time import sleep
from pynput import mouse,keyboard
from pynput.mouse import Button
from pynput.keyboard import Key

class Controller:
    def __init__(self,json):
        self.mouse = mouse.Controller()
        self.keybord = keyboard.Controller()
        self.json_name = json
        self.steps  = []

    def wait(self, fun):
        """Decorator to wait 1.5s"""
        def wrapper(*args, **kwargs):
            sleep(1.5)
            return fun(*args, **kwargs)
        return wrapper

    @wait
    def clik_button(self, key):
        with self.keybord.pressed(key):
            pass

    @wait
    def press_button(self, key):
        self.keybord.press(key)

    @wait
    def release(self,key):
        self.keybord.release(key)

    @wait
    def hold_and_press(self,key_hold, key_press):
        with self.keybord.pressed(key_hold):
            self.keybord.press(key_press)

    def load_steps(self):
        with open(self.json_name,'r', encoding='UTF-8') as file:
            self.steps = json.load(file)['STEPS']

    @wait
    def type(self, text):
        self.keybord.type(text)

    def draw_line(self, x, y, dx):
        self.mouse.position = (x, y)
        self.mouse.press(Button.left)
        for _ in range(0, int(dx)):
            self.mouse.move(1, 0)
            sleep(0.01)
        self.mouse.release(Button.left)











if __name__=='__main__':
    Contoller()