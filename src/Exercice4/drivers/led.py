from constants.colors import *


class Led:
    def __init__(self, pin):
        self.pin = pin
        self.currentColor = BLACK

    def on(self):
        self.currentColor = WHITE
        self.pin.pixels_fill(self.currentColor)
        self.pin.pixels_show()

    def off(self):
        self.currentColor = BLACK
        self.pin.pixels_fill(self.currentColor)
        self.pin.pixels_show()

    def set_color(self, color):
        self.currentColor = color
        self.pin.pixels_fill(self.currentColor)
        self.pin.pixels_show()
