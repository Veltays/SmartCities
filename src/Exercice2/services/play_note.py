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



    def au_clair_de_la_lune(self):
        notes = [
            NOTE_DO, NOTE_DO, NOTE_DO, NOTE_RE, NOTE_MI,
            NOTE_RE, NOTE_DO, NOTE_MI, NOTE_RE, NOTE_RE, NOTE_DO,

            NOTE_RE, NOTE_RE, NOTE_RE, NOTE_RE, NOTE_LA,
            NOTE_LA, NOTE_RE, NOTE_DO, NOTE_SI, NOTE_LA, NOTE_SO
        ]

        durations = [
            0.30, 0.30, 0.30, 0.30, 0.60,
            0.30, 0.30, 0.30, 0.30, 0.30, 0.60,

            0.30, 0.30, 0.30, 0.30, 0.60,
            0.30, 0.30, 0.30, 0.30, 0.30, 0.90
        ]

        for note, duration in zip(notes, durations):
            volume = self.myPotentiometer.getValue()
            self.play_note(note, volume, duration)
            
    def frere_jacques(self):
        notes = [
            NOTE_DO, NOTE_RE, NOTE_MI, NOTE_DO,
            NOTE_DO, NOTE_RE, NOTE_MI, NOTE_DO,

            NOTE_MI, NOTE_FA, NOTE_SO,
            NOTE_MI, NOTE_FA, NOTE_SO,

            NOTE_SO, NOTE_LA, NOTE_SO, NOTE_FA, NOTE_MI, NOTE_DO,
            NOTE_SO, NOTE_LA, NOTE_SO, NOTE_FA, NOTE_MI, NOTE_DO,

            NOTE_DO, NOTE_SO, NOTE_DO,
            NOTE_DO, NOTE_SO, NOTE_DO
        ]

        durations = [
            0.30, 0.30, 0.30, 0.60,
            0.30, 0.30, 0.30, 0.60,

            0.30, 0.30, 0.60,
            0.30, 0.30, 0.60,

            0.15, 0.15, 0.15, 0.15, 0.30, 0.60,
            0.15, 0.15, 0.15, 0.15, 0.30, 0.60,

            0.30, 0.30, 0.60,
            0.30, 0.30, 0.60
        ]

        for note, duration in zip(notes, durations):
            volume = self.myPotentiometer.getValue()
            self.play_note(note, volume, duration)