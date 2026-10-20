from library.ws2812 import WS2812
from constants.pin import PIN_LED_WS

LED_COUNT = 1
led = WS2812(pin_num=PIN_LED_WS, led_count=1)
