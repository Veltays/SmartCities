from constants.note import *

class PlayNote():

    def __init__(self,MyBuzzer,timer,myPotentiometer):
        self.myBuzzer = MyBuzzer
        self.myTimer = timer
        self.myPotentiometer = myPotentiometer


    def play_note(self, note, volume, duration):
        self.myBuzzer.set_frequency(note)
        self.myBuzzer.set_volume(volume)

        self.myTimer.sleep(duration * 0.9)

        self.myBuzzer.set_volume(0)
        self.myTimer.sleep(duration * 0.1)



    def one_piece_song(self):
        notes = [
            NOTE_LA, NOTE_LA, NOTE_SO,
            NOTE_SO, NOTE_MI, NOTE_DO, NOTE_LA,
            NOTE_LA, NOTE_MI, NOTE_RE,
            NOTE_SO, NOTE_LA
        ]

        durations = [
            0.30, 0.30, 0.60,
            0.30, 0.30, 0.30, 0.60,
            0.30, 0.30, 0.60,
            0.30, 0.90
        ]
        for note, duration in zip(notes, durations):
            volume = self.myPotentiometer.getValue()
            print("Valeur du potentio",self.myPotentiometer.getCurrentValue())
            self.play_note(note, volume, duration)