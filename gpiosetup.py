import RPi.GPIO as GPIO

def gpioInit():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(26,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(13,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(19,GPIO.OUT)
    # GPIO.setup(38,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(12,GPIO.IN)
    GPIO.setup(21,GPIO.IN)