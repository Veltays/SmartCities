from constants.pin import * 
import machine
from library.lcd1602 import LCD1602



SCL_FREQ = 4000
ID_SCREEN = 1

I2C_LCD_SCREEN = machine.I2C(ID_SCREEN,scl=SCL_PIN,sda=SDA_PIN,freq=SCL_FREQ)





NUMBER_OF_LINES = 2
NUMBER_OF_CHAR_PER_LINE = 16

LCD_SCREEN_PIN = LCD1602(i2c=I2C_LCD_SCREEN,lines=NUMBER_OF_LINES,dotsize=NUMBER_OF_CHAR_PER_LINE)
