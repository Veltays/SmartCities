import machine
# Généré un signal numériques
BUZZER_PIN = machine.PWM(machine.Pin(27, machine.Pin.OUT))


# Tensions analogique (convertie en numérique)
POTENTIOMER_PIN = machine.ADC(machine.Pin(26))

# Pin LCD
SCL_PIN = machine.Pin(7)
SDA_PIN = machine.Pin(6)


# Pin COMPONENT
LED_PIN = machine.Pin(18, machine.Pin.OUT)
BUTTON_PIN = machine.Pin(16, machine.Pin.IN)

