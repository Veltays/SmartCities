from constants.pin import * 
import machine
from library.lcd1602 import LCD1602



ID_I2C = 1
SCL_FREQ = 100000

I2C_LCD = machine.I2C(ID_I2C,scl=I2C1_SCL_PIN,sda=I2C1_SDA_PIN,freq=SCL_FREQ)





NUMBER_OF_LINES = 2
NUMBER_OF_CHAR_PER_LINE = 16

LCD_SCREEN = LCD1602(i2c=I2C_LCD,lines=NUMBER_OF_LINES,dotsize=NUMBER_OF_CHAR_PER_LINE)







