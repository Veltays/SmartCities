from constants.led import led as ledws_pin
from constants.colors import *
from services.timer import Timer
from constants.pin import SOUND_SENSOR_PIN
from drivers.led import Led
from drivers.soundSensor import SoundSensor
from random import choice


def setup():
    timer = Timer()
    led = Led(ledws_pin)
    soundSensor = SoundSensor(SOUND_SENSOR_PIN, timer=timer)

    return led, timer, soundSensor


def loop(led, timer, soundSensor):
    threshold = 20
    last_beat = timer.ticks_ms()

    while True:
        sound = soundSensor.read_sound()

        if sound > threshold:
            current_time = timer.ticks_ms()

            if timer.ticks_diff(current_time, last_beat) >= 150:
                led.set_color(choice(COLORS))
                last_beat = current_time

        print("son :", sound)


if __name__ == "__main__":
    led, timer, soundSensor = setup()
    loop(led, timer, soundSensor)
