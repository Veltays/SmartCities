import utime
from constantes.pin import LED_PIN
from drivers.led import led

myLed = led(LED_PIN)

while True:
    myLed.toggle()
    utime.sleep(2)