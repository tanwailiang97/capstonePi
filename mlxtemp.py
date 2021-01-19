import RPi.GPIO as GPIO
from smbus2 import SMBus
from mlx90614 import MLX90614

count = 0
rate = 1.52
def getTemp():
    bus = SMBus(1)
    sensor = MLX90614(bus, address = 0x5A)
    ambTemp = sensor.read_temp(sensor.MLX90614_TA)
    objTemp = sensor.read_temp(sensor.MLX90614_TOBJ1)
   # if count == 0:
   #     rate = (objTemp+(objTemp-ambTemp))/36.98
   #     count = 1
    objTemp = objTemp + (objTemp-ambTemp)/rate
    bus.close()
    return objTemp
    
