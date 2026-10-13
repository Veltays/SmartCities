from constants.pin import *
import machine
from drivers.potentiometer import Potentiemer
from drivers.buzzer import Buzzer
from drivers.led import Led
from drivers.lcd import LCD
from services.timer import Timer
from constants.screen import LCD_SCREEN
from constants.temp_sensor import HUMIDITY_SENSOR
from constants.constants import *
from services.screen_service import *

ALARM_IS_ON = False


def handleTemperature(temperature, temp_consigne, myBuzzer, myLed, LCDScreen):
    global ALARM_IS_ON
    difference = temperature - temp_consigne

    if difference < THRESHOLD_MAX_LIMIT:
        ALARM_IS_ON = True
        myBuzzer.buzz()
        myLed.toggle()
        if MODE == 1:
            blinkAlarm(LCDScreen)
        elif MODE == 2:
            display_alarm_scroll(LCDScreen)
        return 200

    elif difference <= THRESHOLD_LIMIT:
        ALARM_IS_ON = False
        myBuzzer.stop_buzzer()
        myLed.toggle()
        return 500

    else:
        ALARM_IS_ON = False
        myLed.off()
        myBuzzer.stop_buzzer()
        return 500


# Setup
def setup():
    # Créations du drivers du Buzzer pour le controller
    myBuzzer = Buzzer(BUZZER_PIN)

    # Créations du drivers de ma led
    myLed = Led(LED_PIN)
    LCDScreen = LCD(LCD_SCREEN)

    timer = Timer()
    # Créations du drivers de mon potentiometre
    myPotentiometer = Potentiemer(POTENTIOMER_PIN)

    return myPotentiometer, LCDScreen, timer, myLed, myBuzzer


def loop(myPotentiometer, LCDScreen, timer, myLed, myBuzzer):
    global ALARM_IS_ON
    while True:

        temp_consigne = myPotentiometer.getValue()
        temperature = HUMIDITY_SENSOR.dht20_temperature()

        if not ALARM_IS_ON:
            display_screen(temperature, temp_consigne, LCDScreen)

        frequency = handleTemperature(
            temperature,
            temp_consigne,
            myBuzzer,
            myLed,
            LCDScreen,
        )

        timer.sleep_hertz(frequency)


if __name__ == "__main__":
    myPotentiometer, LCDScreen, timer, myLed, myBuzzer = setup()
    loop(myPotentiometer, LCDScreen, timer, myLed, myBuzzer)
