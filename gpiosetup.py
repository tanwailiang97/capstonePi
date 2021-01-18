import RPi.GPIO as GPIO

def gpioInit():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(37,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(33,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(12,GPIO.OUT)
    # GPIO.setup(38,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(26,GPIO.IN)
    GPIO.setup(40,GPIO.IN)