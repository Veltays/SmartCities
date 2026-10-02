from constants.pin import BUZZER_PIN, POTENTIOMER_PIN
from constants.note import *


from drivers.buzzer import Buzzer
from services.play_note import PlayNote
from services.timer import Timer



def setup():
    myBuzzer = Buzzer(BUZZER_PIN)
    myTimer = Timer()
    myPlayer = PlayNote(myBuzzer,myTimer)
    return myBuzzer, myPlayer,myTimer

def loop(myBuzzer,myPlayerNote,myTimer):

    while True:
        myBuzzer.set_frequency(0)
        myBuzzer.set_volume(0)
        myBuzzer.stop_buzzer()


        myPlayerNote.one_piece_song()


        


if __name__ == "__main__":
    myBuzzer,myPlayer,myTimer = setup()
    loop(myBuzzer,myPlayer,myTimer)
