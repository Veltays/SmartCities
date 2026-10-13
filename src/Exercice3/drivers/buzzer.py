import machine


class Buzzer:

     ALARM_FREQUENCY = 2500
     ALARM_VOLUME = 32768
     ALARM_STEP_MS = 500

     def __init__(self, pin):
          self.myBuzzer = pin
          self.alarm_timer = machine.Timer(-1)
          self.alarm_active = False
          self.alarm_step = 0
          self.stop_buzzer()

     def set_volume(self,volume):
          self.myBuzzer.duty_u16(volume)


     def set_frequency(self,frequency):
          self.myBuzzer.freq(frequency)


     def stop_buzzer(self):
          self.set_volume(0)


     def buzz(self,volume = 65535, frequency = 2500):
          self.set_frequency(frequency)
          self.set_volume(volume)


     def start_alarm(self):
          if self.alarm_active:
               return

          self.alarm_active = True
          self.alarm_step = 0
          self.buzz(
               volume=self.ALARM_VOLUME,
               frequency=self.ALARM_FREQUENCY,
          )
          self.alarm_timer.init(
               period=self.ALARM_STEP_MS,
               mode=machine.Timer.PERIODIC,
               callback=self._update_alarm,
          )


     def stop_alarm(self):
          if self.alarm_active:
               self.alarm_active = False
               self.alarm_timer.deinit()

          self.alarm_step = 0
          self.stop_buzzer()


     def _update_alarm(self, timer):
          if not self.alarm_active:
               return

          self.alarm_step = (self.alarm_step + 1) % 3

          if self.alarm_step == 2:
               self.stop_buzzer()
          elif self.alarm_step == 0:
               self.buzz(
                    volume=self.ALARM_VOLUME,
                    frequency=self.ALARM_FREQUENCY,
               )
