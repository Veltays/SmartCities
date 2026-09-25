class led:
    def __init__(self, pin,timer):
        self.pin = pin
        self.state = False
        self.currentValue = 1
        self.timer = timer



    #*==========================================*#
    #          GETTER AND SETTER                 #
    #*==========================================*#



    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

        if self.get_state() == True:
             self.set_value(1)
        else:
             self.set_value(0)


    # permet de définir la valeur de la LED
    def set_value(self, value):
        # Vérifie que la valeur est comprise entre 0 et 1         
        if(value == 0 or value == 1):
            self.currentValue = value
            self.pin.value(self.currentValue)
        else:
            print("Value must be between 0 and 1")
            return


    def get_value(self):
        return self.currentValue


    #*==========================================*#
    #          GESTION DE L'ETAT DE LA LED        #
    #*==========================================*#

    
    def on(self):
        self.set_state(True)
        

    def off(self):
        self.set_state(False)

    def toggle(self):
        if self.get_state() == True:
            self.off()
        else:
            self.on()


