class SoundSensor:

    def __init__(self, pin, timer):
        self.pin = pin
        self.timer = timer

    def read_sound(self):
        start = self.timer.ticks_ms()
        max_sound = 0

        while self.timer.ticks_diff(self.timer.ticks_ms(), start) < 30:
            value = self.pin.read_u16() / 256
            max_sound = max(max_sound, value)

        return max_sound
