import machine
from constants.constants import * 



class Potentiemer:

    def __init__(self, pin):
        self.potentiometer = pin
        self.timer = machine.Timer(-1)
        self.currentValue = 0

    def getValue(self):
        self.currentValue = self.potentiometer.read_u16()
        return round(TEMPERATURE_MIN + (self.currentValue / MAX_ADC) * TEMPERATURE_ECART)

    def start_interrupt(self, callback):
        self.timer.init(
            period=100,
            mode=machine.Timer.PERIODIC,
            callback=callback
        )

    def getCurrentValue(self):
        return self.currentValue

    