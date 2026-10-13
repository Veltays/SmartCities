class Led:
    def __init__(self, pin):
        self.pin = pin
        self.state = False
        self.currentValue = 0

        self.brightness = 0
        self.step = 1000

        self.off()

    # GETTER AND SETTER

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

        if self.state:
            self.set_value(65535)
        else:
            self.set_value(0)

    def set_value(self, value):
        if 0 <= value <= 65535:
            self.currentValue = value
            self.pin.duty_u16(value)
        else:
            print("Value must be between 0 and 65535")

    def get_value(self):
        return self.currentValue

    # GESTION DE L'ETAT DE LA LED

    def on(self):
        self.set_state(True)

    def off(self):
        self.set_state(False)

    def toggle(self):
        if self.get_state():
            self.off()
        else:
            self.on()

    # DIMMER

    def dimmer(self):
        self.brightness += self.step

        if self.brightness >= 65535:
            self.brightness = 65535
            self.step = -1000

        elif self.brightness <= 0:
            self.brightness = 0
            self.step = 1000

        self.set_value(self.brightness)

    def reset_dimmer(self):
        self.brightness = 0
        self.step = 1000
        self.off()
