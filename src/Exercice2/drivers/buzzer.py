class Buzzer:

     def __init__(self, pin):
          self.myBuzzer = pin

     def set_volume(self,volume):
          self.myBuzzer.duty_u16(volume)


     def set_frequency(self,frequency):
          self.myBuzzer.freq(frequency)


     def stop_buzzer(self):
          self.set_volume(0)
          self.set_frequency(0)