import RPi.GPIO as GPIO
from time import sleep
from .mlxtemp import updateTemp

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(36,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(38,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(40,GPIO.IN)
GPIO.add_event_detect(40,GPIO.FALLING,callback = updateTemp)

while True:
    sleep(0.5)