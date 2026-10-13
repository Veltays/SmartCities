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




def display_screen(temperature, conditionTemperature,LCDScreen):
    LCDScreen.clear_and_reset_cursor()
    LCDScreen.write(f"Set :{conditionTemperature}")
    LCDScreen.set_cursor(1,0)
    LCDScreen.write(f"Ambient :{round(temperature)}")



def handleTemperature(temperature,temp_consigne,myBuzzer,myLed,LCDScreen):


            difference = temperature - temp_consigne

            if difference < THRESHOLD_MAX_LIMIT:
                print("ALARME")
                myBuzzer.buzz()
                myLed.toggle()
                LCDScreen.clear_and_reset_cursor()
                LCDScreen.write("ALARM")
                return 200
    
            elif(difference <= THRESHOLD_LIMIT):
                myBuzzer.stop_buzzer()
                print("pas depassement")
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

    return myPotentiometer,LCDScreen,timer,myLed,myBuzzer



def loop(myPotentiometer,LCDScreen,timer,myLed,myBuzzer):
    while True:


        temp_consigne = myPotentiometer.getValue()
        temperature = HUMIDITY_SENSOR.dht20_temperature()




        display_screen(temperature, temp_consigne,LCDScreen)



        frequency = handleTemperature(temperature,temp_consigne,myBuzzer,myLed,LCDScreen,)

        timer.sleep_hertz(frequency)


if __name__ == "__main__":
    myPotentiometer,LCDScreen,timer,myLed,myBuzzer = setup()       
    loop(myPotentiometer,LCDScreen,timer,myLed,myBuzzer)




