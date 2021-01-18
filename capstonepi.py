import RPi.GPIO as GPIO
from time import sleep, localtime
from mlxtemp import getTemp
from gpiosetup import gpioInit
from tm1637 import TM1637



gpioInit()
GPIO.add_event_detect(40,GPIO.FALLING,callback = updateTemp)

DIO = 16
CLK = 20
mTemp = 0
def updateTemp(channel):
    tempList = []
    while not GPIO.input(40):
        tempList.append(getTemp())
    if len(tempList)>0:
        outTemp = statistics.median(tempList)
        print(outTemp)
        mTemp = int(outTemp*100+0.5)

if __name__ == '__main__':
    tm = TM1637(CLK, DIO)
    tm.brightness(1)

    # clock = Clock(tm)
    # clock.run()

while True:
    sleep(0.5)
    tm.show(mTemp, True)

