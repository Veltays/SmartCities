import machine

BUZZER_PIN = machine.PWM(machine.Pin(27, machine.Pin.OUT))
POTENTIOMER_PIN = machine.ADC(machine.Pin(26))


LED_PIN = machine.Pin(18, machine.Pin.OUT)
BUTTON_PIN = machine.Pin(16, machine.Pin.IN)

