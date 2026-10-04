from constants.pin import *
from constants.note import *
from constants.time import *

import machine
from drivers.buzzer import Buzzer
from drivers.led import Led
from drivers.potentiometer import Potentiemer
from services.player_note import PlayerNote
from services.timer import Timer



from interrupts.button_interrupt import ButtonInterrupt







# Setup
def setup():
    # Créations du drivers du Buzzer pour le controller
    myBuzzer = Buzzer(BUZZER_PIN)

    myTimer = Timer()

    myButtonInterrupt = ButtonInterrupt(BUTTON_PIN,myTimer)



    # Créations du drivers de ma led
    myLed = Led(LED_PIN)


    # Créations du drivers de mon potentiometre
    myPotentiometer = Potentiemer(POTENTIOMER_PIN)


    myPlayer = PlayerNote(myBuzzer,myTimer,myPotentiometer,myLed)



    return myPlayer, myButtonInterrupt




def loop(myPlayerNote,myButtonInterrupt):
    while True:
        myPlayer.chooseMusic(
            myButtonInterrupt.choice,
            myButtonInterrupt
        )



if __name__ == "__main__":
    myPlayer,myButtonInterrupt = setup()
    loop(myPlayer,myButtonInterrupt)



