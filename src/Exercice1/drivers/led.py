class led:
    def __init__(self, pin):
        self.pin = pin
        self.state = False

    def on(self):
        self.pin.value(1)
        self.state = True

    def off(self):
        self.pin.value(0)
        self.state = False

    def toggle(self):
        if self.state:
            self.off()
        else:
            self.on()