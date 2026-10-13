currentLoop = 0


index = 0
word = ["A", "L", "A", "R", "M"]


def display_alarm_scroll(LCDScreen):
    global index

    if index >= len(word):
        index = 0
        LCDScreen.clear_and_reset_cursor()

    print(f"Current Letter - {word[index]} - Index - {index}")

    LCDScreen.set_cursor(index, 0)
    LCDScreen.write(word[index])

    index += 1


def display_screen(temperature, conditionTemperature, LCDScreen):
    global currentLoop

    LCDScreen.clear_and_reset_cursor()
    LCDScreen.write(f"Set :{conditionTemperature}")
    LCDScreen.set_cursor(1, 0)
    LCDScreen.write(f"Ambient :{round(temperature)}")


def blinkAlarm(LCDScreen):
    global currentLoop

    if (currentLoop % 2) == 0:
        LCDScreen.write(f"ALARM")
        print(f"UNCLEAR - current loop {currentLoop}")
        currentLoop += 1

    elif currentLoop == 1:
        print(f"CLEAR - current loop {currentLoop}")
        LCDScreen.clear_and_reset_cursor()
        currentLoop = 0
