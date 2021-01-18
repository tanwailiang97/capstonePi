import RPi.GPIO as GPIO
from time import sleep, localtime, time
from mlxtemp import getTemp
from gpiosetup import gpioInit
from tm1637 import TM1637
import statistics

gpioInit()
DIO = 16
CLK = 20
prevTime = 0
mTemp = [0,0]

if __name__ == '__main__':
    tm = TM1637(CLK, DIO)
    pwm = GPIO.PWM(19, 1000)
    pwm.start(0)

def updateTemp(channel):
    tempList = []
    while not GPIO.input(21):
        tempList.append(getTemp())
    if len(tempList)>0:
        outTemp = statistics.median(tempList)
        print(outTemp)
        if outTemp > 35.0 :
            mTemp[0] = int(outTemp)
            mTemp[1] = int((outTemp*100+0.5)%100)
            tm.numbers(mTemp[0],mTemp[1],True)
            tm.brightness(1)
            prevTime = time() + 1.5

def motorTurn(channel):
    pwm.ChangeDutyCycle(50)
    sleep(0.2)
    pwm.ChangeDutyCycle(0)

GPIO.add_event_detect(12,GPIO.FALLING,callback = motorTurn)
GPIO.add_event_detect(21,GPIO.FALLING,callback = updateTemp)

while True:
    if time() - prevTime > 0.5 :
        prevTime = time()
        tm.numbers(mTemp[0],mTemp[1],True)
        tm.brightness(0)
    #sleep(0.5)

