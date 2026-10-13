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

currentLoop = 0


def display_screen(temperature, conditionTemperature, LCDScreen):
    global currentLoop

    LCDScreen.clear_and_reset_cursor()
    LCDScreen.write(f"Set :{conditionTemperature}")
    LCDScreen.set_cursor(1, 0)
    LCDScreen.write(f"Ambient :{round(temperature)}")


def blinkAlarm(LCDScreen):
    global currentLoop

    if (currentLoop % 2) == 0:
        LCDScreen.write(f"ALARM")
        print(f"UNCLEAR - current loop {currentLoop}")
        currentLoop += 1

    elif currentLoop == 1:
        print(f"CLEAR - current loop {currentLoop}")
        LCDScreen.clear_and_reset_cursor()
        currentLoop = 0


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
    while True:

        temp_consigne = myPotentiometer.getValue()
        temperature = HUMIDITY_SENSOR.dht20_temperature()

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
