from constants.pin import * 
import machine

from library.dht20 import *

ID_I2C = 0
SCL_FREQ = 100000

I2C_HUMIDITY_SENSOR = machine.I2C(ID_I2C,scl=I2C0_SCL_PIN,sda=I2C0_SDA_PIN,freq=SCL_FREQ)


HUMIDITY_SENSOR = DHT20(I2C_HUMIDITY_SENSOR)


