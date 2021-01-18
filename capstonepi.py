import RPi.GPIO as GPIO
from time import sleep, localtime
from mlxtemp import getTemp
from gpiosetup import gpioInit
from tm1637 import TM1637
import statistics



gpioInit()
DIO = 16
CLK = 20
mTemp = []

def updateTemp(channel):
    tempList = []
    while not GPIO.input(40):
        tempList.append(getTemp())
    if len(tempList)>0:
        outTemp = statistics.median(tempList)
        print(outTemp)
        mTemp[0] = int(outTemp)
        mTemp[1] = int((outTemp*100%100)+0.5)

GPIO.add_event_detect(40,GPIO.FALLING,callback = updateTemp)

if __name__ == '__main__':
    tm = TM1637(CLK, DIO)
    tm.brightness(1)

    # clock = Clock(tm)
    # clock.run()

while True:
    sleep(0.5)
    tm.numbers(mTemp[0],mTemp[1] True)

