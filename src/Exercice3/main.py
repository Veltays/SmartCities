from constants.pin import *
import machine
from drivers.potentiometer import Potentiemer
from drivers.buzzer import Buzzer
from drivers.led import Led
from drivers.lcd import LCD
from services.timer import Timer
from constants.screen import LCD_SCREEN
from constants.temp_sensor import HUMIDITY_SENSOR




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

    return myPotentiometer,LCDScreen,timer,myLed,myBuzzer






def loop(myPotentiometer,LCDScreen,timer,myLed,myBuzzer):
    while True:



        LCDScreen.clear_and_reset_cursor()




        temp_consigne = myPotentiometer.getValue()
        LCDScreen.write(temp_consigne)

        temperature = HUMIDITY_SENSOR.dht20_temperature()
        humidity = HUMIDITY_SENSOR.dht20_humidity()


        print(f"Current value desired {temp_consigne} \n current Temperature {temperature} \n humidity {humidity} \n ------------------------------------------------------------------- ")



        if temperature > (temp_consigne + 3):
            print("depassement")
            myBuzzer.start_alarm()
            myLed.toggle()
            LCDScreen.clear_and_reset_cursor()
            LCDScreen.write("ALARM")

        elif temperature > temp_consigne:
            myBuzzer.stop_alarm()
            print("pas depassement")
            myLed.toggle()

        else:
            myBuzzer.stop_alarm()




        timer.sleep(1)


if __name__ == "__main__":
    myPotentiometer,LCDScreen,timer,myLed,myBuzzer = setup()       
    loop(myPotentiometer,LCDScreen,timer,myLed,myBuzzer)




