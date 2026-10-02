from constants.pin import BUZZER_PIN, POTENTIOMER_PIN
from constants.note import *


from drivers.buzzer import Buzzer
from drivers.potentiometer import Potentiemer
from services.play_note import PlayNote
from services.timer import Timer





def setup():
    myBuzzer = Buzzer(BUZZER_PIN)
    myTimer = Timer()
    myPotentiometer = Potentiemer(POTENTIOMER_PIN)
    myPlayer = PlayNote(myBuzzer,myTimer,myPotentiometer)
    return myBuzzer, myPlayer,myTimer,myPotentiometer

def loop(myBuzzer,myPlayerNote,myPotentiometer,myTimer):

    while True:
        myBuzzer.set_frequency(0)
        myBuzzer.set_volume(0)
        myBuzzer.stop_buzzer()

        myPlayerNote.one_piece_song()

        print("Valeur du potentio",myPotentiometer.getCurrentValue())

        


if __name__ == "__main__":
    myBuzzer,myPlayer,myTimer,myPotentiometer = setup()
    loop(myBuzzer,myPlayer,myPotentiometer,myTimer)
