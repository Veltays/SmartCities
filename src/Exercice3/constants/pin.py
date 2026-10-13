import machine
from library.dht11 import *


# Généré un signal numériques
BUZZER_PIN = machine.PWM(machine.Pin(27, machine.Pin.OUT))


# Tensions analogique (convertie en numérique)
POTENTIOMER_PIN = machine.ADC(machine.Pin(26))

# Pin LCD
I2C1_SDA_PIN = machine.Pin(6)
I2C1_SCL_PIN = machine.Pin(7)


# Pin Humidity
I2C0_SDA_PIN = machine.Pin(8)
I2C0_SCL_PIN = machine.Pin(9)



# Pin COMPONENT
LED_PIN = machine.Pin(18, machine.Pin.OUT)
BUTTON_PIN = machine.Pin(16, machine.Pin.IN)

