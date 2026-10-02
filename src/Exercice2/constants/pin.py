import machine

BUZZER_PIN = PWM(machine.Pin(18, machine.Pin.OUT))
POTENTIOMER_PIN = machine.Pin(16, machine.Pin.IN)