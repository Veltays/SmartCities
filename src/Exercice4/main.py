from constants.led import led
from constants.colors import COLORS
from services.timer import Timer


def loop():
    timer = Timer()
    while True:
        print("Fills")
        for colors in COLORS:
            led.pixels_fill(colors)
            led.pixels_show()
            timer.sleep(0.2)


if __name__ == "__main__":
    loop()
