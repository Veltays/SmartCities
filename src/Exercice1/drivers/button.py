class button:

    def __init__(self, pin, myTimer):
        self.pin = pin
        self.pin.init(self.pin.IN)
        self.myTimer = myTimer
        self.numberOfPresses = 1

    def is_pressed(self):
        if(self.pin.value() == 1):
           return True
        return False
    

        
