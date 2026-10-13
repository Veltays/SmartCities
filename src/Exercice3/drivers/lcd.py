from constants.screen import *
class LCD:

    def __init__(self,screen):
        self.LCD_SCREEN = screen
        self.row = 0
        self.column = 0



    def write(self,label):
        self.LCD_SCREEN.print(str(label))


    def set_cursor(self,column,row):
        
        if (column >= NUMBER_OF_CHAR_PER_LINE or row >= NUMBER_OF_LINES):
            self.LCD_SCREEN.set_cursor(0,0)
            self.write("OVERFLOW")
            return

        self.row = row
        self.column = column


        self.LCD_SCREEN.setCursor(row, column)



    def clear_screen(self):
        LCD_SCREEN.clear()

        

    def clear_and_reset_cursor(self):
        self.clear_screen()
        self.set_cursor(0,0)



