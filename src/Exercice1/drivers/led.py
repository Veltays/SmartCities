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


    #*==========================================*#
    #          ANIMATIONS DE LA LED              #
    #*==========================================*#

    # Fait clignoter la LED un certain nombre de fois défini par BIP_ITERATION
    def bip(self):
        for _ in range(BIP_ITERATION):
            self.toggle()
            utime.sleep(SLEEP_TIME)


    # Augmente progressivement la luminosité de la LED et la diminue ensuite
    def fade_in_out(self):
        
        print("Gradiants")



    # permet de définir la valeur de la LED
    def set_value(self, value):
        # Vérifie que la valeur est comprise entre 0 et 255         
        if(value > 0 and value < 255):
            self.currentValue = value
        else:
            return
            

