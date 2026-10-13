class Buzzer:

    def __init__(self, pin):
        self.myBuzzer = pin
        self.stop_buzzer()

    def set_volume(self, volume):
        self.myBuzzer.duty_u16(int(volume))

    def set_frequency(self, frequency):
        self.myBuzzer.freq(frequency)

    def stop_buzzer(self):
        self.set_volume(0)
        self.set_frequency(0)

    def buzz(self, volume=32768, frequency=2500):
        self.set_frequency(frequency)
        self.set_volume(volume)