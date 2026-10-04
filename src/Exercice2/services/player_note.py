from constants.note import *
from constants.choice import *

class PlayerNote():

    def __init__(self,MyBuzzer,timer,myPotentiometer,myLed):
        self.myBuzzer = MyBuzzer
        self.myTimer = timer
        self.myPotentiometer = myPotentiometer
        self.myLed = myLed


    def play_note(self, note, volume, duration):

    
        # Définitions des parametre du buzzer
        self.myBuzzer.set_frequency(note)
        self.myBuzzer.set_volume(volume)

        # Activation du buzzer et des led
        self.myLed.on()
        self.myTimer.sleep(duration * 0.9)
        self.myLed.off()

        # Tempo
        self.myBuzzer.set_volume(0)
        self.myTimer.sleep(duration * 0.1)




    def play_music(self, notes, durations, expected_choice, button_interrupt):

        for note, duration in zip(notes, durations):


            if button_interrupt.choice != expected_choice:
                return
            volume = self.myPotentiometer.getValue()

            self.play_note(
                note,
                volume,
                duration
            )
    def frere_jacques(self, get_choice):

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

        self.play_music(
            notes,
            durations,
            CHOICE_FRERE_JACQUES,
            get_choice
        )
                
    def au_clair_de_la_lune(self, get_choice):

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

        self.play_music(
            notes,
            durations,
            CHOICE_AU_CLAIR_DE_LA_LUNE,
            get_choice
        )



    def chooseMusic(self, choice, get_choice):

        if choice == CHOICE_FRERE_JACQUES:
            print("currently playing Frere Jacques")
            self.frere_jacques(get_choice)

        elif choice == CHOICE_AU_CLAIR_DE_LA_LUNE:
            print("currently playing Au clair de la lune")
            self.au_clair_de_la_lune(get_choice)