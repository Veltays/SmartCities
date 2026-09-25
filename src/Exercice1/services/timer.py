from constantes.time import SLEEP_TIME
import utime

class timer:

    def __init__(self):
        self.start_time = 0
        self.end_time = 0


    def start(self):
        self.start_time = utime.ticks_ms()

    def stop(self):
        self.end_time = utime.ticks_ms()
        return utime.ticks_diff(self.end_time, self.start_time)

    def sleep(self, duration = SLEEP_TIME):
        utime.sleep(duration)