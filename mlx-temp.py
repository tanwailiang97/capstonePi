import statistics
import RPi.GPIO as GPIO
from smbus2 import smbus2
from mlx90614 import mlx90614

def getTemp():
    bus = SMBus(1)
    sensor = MLX90614(bus, address = 0x5A)
    ambTemp = sensor.read_temp(sensor.MLX90614_TA)
    objTemp = sensor.read_temp(sensor.MLX90614_TOBJ1)
    objTemp = objTemp + (objTemp-ambTemp)/1.53
    bus.close()
    return objTemp
    
def updateTemp(channel):
    tempList = []
    while not GPIO.input(40):
        tempList.append(getTemp())
    if len(tempList>0):
        outTemp = statistics.median(tempList)
        print(outTemp)
        return outTemp