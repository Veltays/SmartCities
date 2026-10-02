class button:

    def __init__(self, pin):
        self.pin = pin
        self.pin.init(self.pin.IN)

    def is_pressed(self):
        if(self.pin.value() == 1):
           return True
        return False
    

        
