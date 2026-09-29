def effect_TicTicBoom(myLed, myTimer,myButton):

        currentTiming = 1


        while currentTiming > 0 :
            myLed.toggle()
            currentTiming -= 0.05
            if(myTimer.sleep_listening(currentTiming, myButton) == False):
                return



def effect_blink(myLed, myTimer,myButton):
    myLed.on()

    while True:
        if(myTimer.sleep_listening(0.5, myButton) == False):
            break 

    myLed.off()
    
    return