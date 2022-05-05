from pynput import mouse
import time


class MouseControl:
    def __init__(self):
        self.m = mouse.Controller()

    def set_position(self, x, y):
        self.m.position = (x, y)
