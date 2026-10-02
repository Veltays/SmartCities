from constants.pin import BUZZER_PIN, POTENTIOMER_PIN,BUTTON_PIN
from constants.note import *
import machine
from drivers.button import Button
from drivers.buzzer import Buzzer
from drivers.potentiometer import Potentiemer
from services.play_note import PlayNote
from services.timer import Timer
    
choice = 1

def interrupt_handler(pin):
    global choice
    if(choice < 2):
        choice = choice + 1
    else:
        choice = 1
    


def setup():
    myBuzzer = Buzzer(BUZZER_PIN)
    BUTTON_PIN.irq(
    trigger=machine.Pin.IRQ_FALLING,
    handler=interrupt_handler
)
    myButton = Button(BUTTON_PIN)
    myTimer = Timer()
    myPotentiometer = Potentiemer(POTENTIOMER_PIN)
    myPlayer = PlayNote(myBuzzer,myTimer,myPotentiometer)
    return myPlayer,myPotentiometer,myButton

def loop(myPlayerNote,myPotentiometer):
    global choice
    while True:
        chooseMusic(choice,myPlayerNote)


        print("Valeur du potentio",myPotentiometer.getCurrentValue())

        

def chooseMusic(choice,myPlayerNote):
        print("Your choice is",choice)
        if choice == 1:
            myPlayerNote.au_clair_de_la_lune()
        elif choice == 2:
            myPlayerNote.frere_jacques()


if __name__ == "__main__":
    myPlayer,myPotentiometer,myButton = setup()
    loop(myPlayer,myPotentiometer)



