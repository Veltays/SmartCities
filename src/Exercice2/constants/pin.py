import machine

BUZZER_PIN = machine.PWM(machine.Pin(27, machine.Pin.OUT))
POTENTIOMER_PIN = machine.ADC(machine.Pin(26))


