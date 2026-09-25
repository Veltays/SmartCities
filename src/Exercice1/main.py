from services.timer import timer
from constantes.pin import BUTTON_PIN, LED_PIN
from constantes.press_case import (
    LONG_PRESS_CASE,
    NO_PRESS_CASE,
    SHORT_PRESS_CASE,
    VERY_LONG_PRESS_CASE,
)
from drivers.button import button
from drivers.led import led


def main():

    # Initialisations des composants
    myTimer = timer()
    myLed = led(LED_PIN)
    # Injections de dépendances dans boutons pour gestions des appuies
    myButton = button(BUTTON_PIN,myTimer)



    # Boucle principale
    while True:

        buttonState = myButton.is_pressed()

        if buttonState == SHORT_PRESS_CASE:
            print("Short press detected")
            myLed.bip()

        elif buttonState == LONG_PRESS_CASE:
            print("Long press detected")
            myLed.fade_in_out()
            

        elif buttonState == VERY_LONG_PRESS_CASE:
            print("Very long press detected")
            

        elif buttonState == NO_PRESS_CASE:
            myLed.off()

        myTimer.sleep()





if __name__ == "__main__":
    main()
