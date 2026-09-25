import utime 
from constantes.time import SHORT_PRESS_TIME, LONG_PRESS_TIME, VERY_LONG_PRESS_TIME
from constantes.press_case import NO_PRESS_CASE, SHORT_PRESS_CASE, LONG_PRESS_CASE, VERY_LONG_PRESS_CASE


class button:
    def __init__(self, pin):
        self.pin = pin
        self.pin.init(self.pin.IN)

    def is_pressed(self):
        self.start_timer()

        while(self.pin.value() == 1):
            utime.sleep(0.01)

        timeElapsed = self.end_timer()



        match timeElapsed:
            case timeElapsed if timeElapsed < SHORT_PRESS_TIME:
                return SHORT_PRESS_CASE
            case timeElapsed if timeElapsed < LONG_PRESS_TIME:
                return LONG_PRESS_CASE
            case timeElapsed if timeElapsed < VERY_LONG_PRESS_TIME:
                return VERY_LONG_PRESS_CASE

        return NO_PRESS_CASE



    def start_timer(self):
        self.timer = utime.ticks_ms()



    def end_timer(self):
        return utime.ticks_diff(utime.ticks_ms(), self.timer)
    
