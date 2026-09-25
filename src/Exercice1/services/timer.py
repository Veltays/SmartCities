from constantes.time import *
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

    def sleep_listening(self, duration, button):
         # Dans son attentes il lit la valeur du bouton pour ne pas bloquer le programme
        self.start()
        while(utime.ticks_diff(utime.ticks_ms(), self.start_time) < duration * 1000):
            if button.is_pressed():
                utime.sleep(0.1)  # Petite pause pour éviter qu'il détecte plusieurs appuis en même temps
                return False
            
        return True
        
        