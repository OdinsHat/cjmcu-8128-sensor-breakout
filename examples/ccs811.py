from Adafruit_CCS811 import Adafruit_CCS811

def ccs811example():
    getdata()
    printdata()

def getdata():
    """Get the data from the CCS811 sensor module and return it"""
    ccs = Adafruit_CCS811()
    temp = ccs.calculateTemperature()
    ccs.tempOffset = temp - 25.0
    if ccs.available():
        temp = ccs.calculateTemperature()
    if not ccs.readData():
        c02 = ccs.geteCO2()
        tvoc = ccs.getTVOC()
    else:
        print("Error 
    

while(1):
    if ccs.available():
        temp = ccs.calculateTemperature()
    if not ccs.readData():
        print "CO2: ", ccs.geteCO2(), "ppm, TVOC: ", ccs.getTVOC(), " temp: ", temp
    else:
        print "ERROR!"

if __name__ == '__main__':
    ccs811example()
