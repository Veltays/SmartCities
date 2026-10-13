from constants.constants import *
from services.screen_service import *


def handleTemperature(temperature, temp_consigne, myBuzzer, myLed, LCDScreen):

    difference = temperature - temp_consigne

    if difference < THRESHOLD_MAX_LIMIT:
        myBuzzer.buzz()
        myLed.toggle()
        LCDScreen.clear_and_reset_cursor()
        blinkAlarm(LCDScreen)
        return 200

    elif difference <= THRESHOLD_LIMIT:
        myBuzzer.stop_buzzer()
        myLed.toggle()
        return 500

    else:
        myLed.off()
        myBuzzer.stop_buzzer()
        return 500
