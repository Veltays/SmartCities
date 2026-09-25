import utime 
from constantes.time import SHORT_PRESS_TIME, LONG_PRESS_TIME, VERY_LONG_PRESS_TIME, SLEEP_TIME
from constantes.press_case import NO_PRESS_CASE, SHORT_PRESS_CASE, LONG_PRESS_CASE, VERY_LONG_PRESS_CASE




class button:



    def __init__(self, pin, myTimer):
        self.pin = pin
        self.pin.init(self.pin.IN)
        self.myTimer = myTimer
        self.numberOfPresses = 0




    def is_pressed(self):

        self.myTimer.start()

        while self.pin.value() == 1:
            utime.sleep(SLEEP_TIME)

        timeElapsed = self.myTimer.stop()

        if timeElapsed < SHORT_PRESS_TIME:
            return NO_PRESS_CASE

        elif timeElapsed < LONG_PRESS_TIME:
            return SHORT_PRESS_CASE

        elif timeElapsed < VERY_LONG_PRESS_TIME:
            return LONG_PRESS_CASE

        else:
            return VERY_LONG_PRESS_CASE