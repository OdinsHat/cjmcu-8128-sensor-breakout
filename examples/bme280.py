#!/usr/bin/env python
from Adafruit_BME280 import *

def bme280example():
    """The main program function
    """
    (temp, pressure, humidity) = getdata()
    printdata(temp, pressure, humidity)

def getdata():
    """The address parameter is important here as most BME/P280 sensors 
    occupy the default 0x77 address as noticed in the Adafruit library.
    This can be easily verified by running i2cdetect -y 1 on your Pi
    """
    sensor = BME280(
            t_mode=BME280_OSAMPLE_8, 
            p_mode=BME280_OSAMPLE_8, 
            h_mode=BME280_OSAMPLE_8, 
            address=0x76
            )

    degrees = sensor.read_temperature()
    pascals = sensor.read_pressure()
    hectopascals = pascals / 100
    humidity = sensor.read_humidity()

    return (degrees, hectopascals, humidity)

def printdata():
    print('Temp      = {0:0.3f} deg C').format(degrees)
    print('Pressure  = {0:0.2f} hPa').format(hectopascals)
    print('Humidity  = {0:0.2f} %').format(humidity)

if __name__ == '__main__':
    bme280example()
