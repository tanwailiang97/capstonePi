import RPi.GPIO as GPIO
from time import sleep, localtime, time
from mlxtemp import getTemp
from gpiosetup import gpioInit
from tm1637 import TM1637
from key import KEY
import requests
import statistics

gpioInit()
url = "http://tanwailiang.ddns.net/phone/temp"
DIO = 16
CLK = 20
prevTime = 0
mTemp = [0,0]
global flag
flag = 0

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
            global flag
            flag = 2
            postObj = {'temp':outTemp, 'token':KEY}
            postReq = requests.post(url, data = postObj)
            print(postReq)

def motorTurn(channel):
    pwm.ChangeDutyCycle(50)
    sleep(0.8)
    pwm.ChangeDutyCycle(0)

GPIO.add_event_detect(12,GPIO.FALLING,callback = motorTurn)
GPIO.add_event_detect(21,GPIO.FALLING,callback = updateTemp)

while True:
    if time() - prevTime > 0.5 :
        if flag == 0:
            tm.write([0,0,0,0])
        elif flag > 0: 
            flag  = flag -1
        prevTime = time()

