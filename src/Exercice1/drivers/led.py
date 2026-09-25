import utime
from constantes.iteration import BIP_ITERATION
from constantes.time import SLEEP_TIME


class led:
    def __init__(self, pin):
        self.pin = pin
        self.state = False
        self.currentValue = 0

    def on(self):
        self.set_value(self.currentValue + 1)
        self.pin.value(self.currentValue)
        self.state = True


    def off(self):
        self.set_value(self.currentValue - 1)
        self.pin.value(self.currentValue)
        self.state = False


    def toggle(self):
        if self.state:
            self.off()
        else:
            self.on()




    def bip(self):
        for _ in range(BIP_ITERATION):
            self.toggle()
            utime.sleep(SLEEP_TIME)


    def gradiants(self):


    def set_value(self, value):
        print("Setting value: " + str(value))
        if(value > 0 and value < 255):
            self.currentValue = value
        else:
            return
            

