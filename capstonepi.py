import RPi.GPIO as GPIO
from time import sleep, localtime
from mlxtemp import updateTemp
from gpiosetup import gpioInit
#from tm1637 import TM1637



gpioInit()
GPIO.add_event_detect(40,GPIO.FALLING,callback = updateTemp)

DIO = 20
CLK = 16

# class Clock:
#     def __init__(self, tm_instance):
#         self.tm = tm_instance
#         self.show_colon = False

#     def run(self):
#         while True:
#             t = localtime()
#             self.show_colon = not self.show_colon
#             tm.numbers(t.tm_hour, t.tm_min, self.show_colon)
#             sleep(1)


# if __name__ == '__main__':
#     tm = TM1637(CLK, DIO)
#     tm.brightness(1)

#     clock = Clock(tm)
#     clock.run()

while True:
    sleep(0.5)

