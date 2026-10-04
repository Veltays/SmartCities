from constants.time import *
from constants.choice import *
import machine
class ButtonInterrupt:

    def __init__(self, pin,timer):
        self.timer = timer
        self.choice = 1
        self.pin = pin
        self.last_interrupt_time = 0

        self.pin.irq(
            trigger=machine.Pin.IRQ_FALLING,
            handler=self.handler
        )




    def handler(self, pin):

        current_time = self.timer.ticks_ms()

        if self.timer.ticks_diff(
            current_time,
            self.last_interrupt_time
        ) < DEBOUNCE_TIME:
            return

        self.last_interrupt_time = current_time

        self.choice = (self.choice % NUMBER_OF_CHOICE) + 1