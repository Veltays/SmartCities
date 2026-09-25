from constantes.time import SLEEP_TIME
from services.timer import timer
from constantes.pin import BUTTON_PIN, LED_PIN
from constantes.config import NUMBER_OF_LEVELS
from services.led_effect import effect_TicTicBoom

from drivers.button import button
from drivers.led import led



def setup():
    # Initialisations des composants
    myTimer = timer()
    myLed = led(LED_PIN,myTimer)
    # Injections de dépendances dans boutons pour gestions des appuies
    myButton = button(BUTTON_PIN,myTimer)

    
    
    return myTimer, myLed, myButton




def loop(myTimer, myLed, myButton):

    LevelNumber = 1

    # Boucle principale
    while True:

        # Gestion de l'appuie sur le bouton
        if(myButton.is_pressed()):
            # Si le bouton est appuyé, on incrémente le niveau et on change l'état de la LED
            LevelNumber = (LevelNumber) % (NUMBER_OF_LEVELS) + 1


        print("Level: ", LevelNumber)


        if LevelNumber == 3:
            myLed.off()
            

        elif LevelNumber == 5:
            effect_TicTicBoom(myLed,myTimer,myButton)

        else:
            myLed.toggle()
            # Créations du délais
            delay = (SLEEP_TIME / LevelNumber)
            print("Delay: ", delay, " seconds")
        
        myTimer.sleep_listening(delay, myButton)



if __name__ == "__main__":
    myTimer, myLed, myButton = setup()
    loop(myTimer, myLed, myButton)
