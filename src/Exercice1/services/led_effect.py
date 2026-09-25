def effect_TicTicBoom(myLed, myTimer,myButton):

        currentFrequency = 1


        while currentFrequency > 0 :
            myLed.toggle()
            currentFrequency -= 0.05
            if(myTimer.sleep_listening(currentFrequency, myButton) == False):
                return
 