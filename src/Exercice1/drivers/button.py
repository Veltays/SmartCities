import utime 
from constantes.time import SHORT_PRESS_TIME, LONG_PRESS_TIME, VERY_LONG_PRESS_TIME, SLEEP_TIME
from constantes.press_case import NO_PRESS_CASE, SHORT_PRESS_CASE, LONG_PRESS_CASE, VERY_LONG_PRESS_CASE


class button:
    def __init__(self, pin, myTimer):
        self.pin = pin
        self.pin.init(self.pin.IN)
        self.myTimer = myTimer


    def is_pressed(self):

        # Timer d'attentes pour déterminer la durée de l'appui sur le boutons
        self.myTimer.start()

        while(self.pin.value() == 1):
            utime.sleep(SLEEP_TIME)

        timeElapsed = self.myTimer.stop()


        match timeElapsed:
            case timeElapsed if timeElapsed < SHORT_PRESS_TIME:
                return SHORT_PRESS_CASE
            case timeElapsed if timeElapsed < LONG_PRESS_TIME:
                return LONG_PRESS_CASE
            case timeElapsed if timeElapsed < VERY_LONG_PRESS_TIME:
                return VERY_LONG_PRESS_CASE

        return NO_PRESS_CASE



