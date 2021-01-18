import RPi.GPIO as GPIO

def gpioInit():
    GPIO.setwarnings(False)
    # GPIO.setmode(GPIO.BOARD)
    GPIO.setup(26,GPIO.OUT,initial=GPIO.LOW)
    # GPIO.setup(36,GPIO.OUT,initial=GPIO.LOW)
    # GPIO.setup(38,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(21,GPIO.IN)