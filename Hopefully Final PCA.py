import RPi.GPIO as GPIO
from time import sleep
import time
import sys
from evdev import InputDevice, categorize, ecodes, InputEvent

# Setup of GPIO pin numbering type
GPIO.setwarnings(False)

#creates object 'gamepad' to store the data
gamepad = InputDevice('/dev/input/event4')

#button code variables (PLEASE CHECK AND CHANGE WHAT IS WRITE AND WHAT ISNT)
BTN_B = 305          #Actually the X Button
BTN_A = 304          #Actually the A button
BTN_C = 306          #Actually the B button
BTN_X = 307          #Actually the Y button
BTN_START = 315      #This is the joystick click


# Assign the pin numberings for the motors
A1 = 6  # pin 6, Backup: 7
A2 = 13 # pin 13, Backup: 22
B1 = 19 # pin 19, Backup: 23 
B2 = 26 # pin 26, Backup: 24
C1 = 12 # pin 12, Backup: 11
C2 = 16 # pin 16, Backup: 10
D1 = 20 # pin 20, Backup: 27
D2 = 21 # pin 21, Backup: 3
GPIO_TRIGGER = 27 #confirmed working
FrontLeftSensor = 17
FrontRightSensor = 5
RightSensor = 22
BackRightSensor = 23
BackLeftSensor = 24
LeftSensor = 27

# Set the GPIO pins to be output in nature
GPIO.setmode(GPIO.BCM)
GPIO.setup(A1, GPIO.OUT)
GPIO.setup(A2, GPIO.OUT)
GPIO.setup(B1, GPIO.OUT)
GPIO.setup(B2, GPIO.OUT)
GPIO.setup(C1, GPIO.OUT)
GPIO.setup(C2, GPIO.OUT)
GPIO.setup(D1, GPIO.OUT)
GPIO.setup(D2, GPIO.OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(FrontLeftSensor, GPIO.IN)
GPIO.setup(FrontRightSensor, GPIO.IN)
GPIO.setup(RightSensor, GPIO.IN)
GPIO.setup(BackRightSensor, GPIO.IN)
GPIO.setup(BackLeftSensor, GPIO.IN)
GPIO.setup(LeftSensor, GPIO.IN)


def backwards():
    GPIO.output(A1, 1)
    GPIO.output(A2, 0)
    GPIO.output(B1, 1)
    GPIO.output(B2, 0)
    GPIO.output(C1, 1)
    GPIO.output(C2, 0)
    GPIO.output(D1, 1)
    GPIO.output(D2, 0)
    sleep(.055)
def forward():
    GPIO.output(A1, 0)
    GPIO.output(A2, 1)
    GPIO.output(B1, 0)
    GPIO.output(B2, 1)
    GPIO.output(C1, 0)
    GPIO.output(C2, 1)
    GPIO.output(D1, 0)
    GPIO.output(D2, 1)
    sleep(.055)
def left():
    GPIO.output(A1, 1)
    GPIO.output(A2, 0)
    GPIO.output(B1, 0)
    GPIO.output(B2, 1)
    GPIO.output(C1, 1)
    GPIO.output(C2, 0)
    GPIO.output(D1, 0)
    GPIO.output(D2, 1)
    sleep(.055)
def right():
    GPIO.output(A1, 0)
    GPIO.output(A2, 1)
    GPIO.output(B1, 1)
    GPIO.output(B2, 0)
    GPIO.output(C1, 0)
    GPIO.output(C2, 1)
    GPIO.output(D1, 1)
    GPIO.output(D2, 0)
    sleep(.055)
def stop():
    GPIO.output(A1, 0)
    GPIO.output(A2, 0)
    GPIO.output(B1, 0)
    GPIO.output(B2, 0)
    GPIO.output(C1, 0)
    GPIO.output(C2, 0)
    GPIO.output(D1, 0)
    GPIO.output(D2, 0)
def distanceFrontLeftSensor():
    distanceFL = 41
#     GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
#     GPIO.output(GPIO_TRIGGER, True)
#     time.sleep(0.00001)
#     GPIO.output(GPIO_TRIGGER, False)
#     StartTime = time.time()
#     StopTime = time.time()
#     while GPIO.input(FrontLeftSensor) == 0:
#         StartTime = time.time()
#     while GPIO.input(FrontLeftSensor) ==1:
#         StopTime = time.time()
#     TimeElapsed = StopTime-StartTime
#     distanceFL = (TimeElapsed*34300) / 2
    return distanceFL
def distanceFrontRightSensor():
    distanceFR = 40
#     GPIO.output(GPIO_TRIGGER, True)
#     time.sleep(0.00001)
#     GPIO.output(GPIO_TRIGGER, False)
#     StartTime = time.time()
#     StopTime = time.time()
#     while GPIO.input(FrontRightSensor) == 0:
#         StartTime = time.time()
#     while GPIO.input(FrontRightSensor) ==1:
#         StopTime = time.time()
#     TimeElapsed = StopTime-StartTime
#     distanceFR = (TimeElapsed*34300) / 2
    return distanceFR    
def distanceRightSensor():
    distanceR =40
#     GPIO.output(GPIO_TRIGGER, True)
#     time.sleep(0.00001)
#     GPIO.output(GPIO_TRIGGER, False)
#     StartTime = time.time()
#     StopTime = time.time()
#     while GPIO.input(RightSensor) == 0:
#         StartTime = time.time()
#     while GPIO.input(RightSensor) ==1:
#         StopTime = time.time()
#     TimeElapsed = StopTime-StartTime
#     distanceR = (TimeElapsed*34300) / 2
    return distanceR   
def distanceBackRightSensor():
    distanceBR = 50
#     GPIO.output(GPIO_TRIGGER, True)
#     time.sleep(0.00001)
#     GPIO.output(GPIO_TRIGGER, False)
#     StartTime = time.time()
#     StopTime = time.time()
#     while GPIO.input(BackRightSensor) == 0:
#         StartTime = time.time()
#     while GPIO.input(BackRightSensor) ==1:
#         StopTime = time.time()
#     TimeElapsed = StopTime-StartTime
#     distanceBR = (TimeElapsed*34300) / 2
    return distanceBR   
def distanceBackLeftSensor():
    distanceBL = 50
#     GPIO.output(GPIO_TRIGGER, True)
#     time.sleep(0.00001)
#     GPIO.output(GPIO_TRIGGER, False)
#     StartTime = time.time()
#     StopTime = time.time()
#     while GPIO.input(BackLeftSensor) == 0:
#         StartTime = time.time()
#     while GPIO.input(BackLeftSensor) ==1:
#         StopTime = time.time()
#     TimeElapsed = StopTime-StartTime
#     distanceBL = (TimeElapsed*34300) / 2
    return distanceBL   
def distanceLeftSensor():
    distanceL =40
#     GPIO.output(GPIO_TRIGGER, True)
#     time.sleep(0.00001)
#     GPIO.output(GPIO_TRIGGER, False)
#     StartTime = time.time()
#     StopTime = time.time()
#     while GPIO.input(LeftSensor) == 0:
#         StartTime = time.time()
#     while GPIO.input(LeftSensor) ==1:
#         StopTime = time.time()
#     TimeElapsed = StopTime-StartTime
#     distanceL = (TimeElapsed*34300) / 2
    return distanceL   


for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
#         if event.value == 1:
        #FORWARD
        if   event.code == BTN_B:
            if (distanceFrontLeftSensor()) > 30:
                if   (distanceFrontRightSensor()) > 30 : #Nothing around, go ham
                    print('Forward')
                    forward()
                else:
                    print ('Object @ F,R')
                    stop()
            else:
                print ('Object @ F,L')
                stop()
        #BACKWARD
        if   event.code == BTN_C:
            if (distanceBackLeftSensor()) > 30:
                if   (distanceBackRightSensor()) > 30 : #Nothing around, go ham
                    print('Backwards')
                    backwards()
                else:
                    print ('Object @ B,R')
                    stop()
            else:
                print ('Object @ B,L')
                stop()
        #RIGHT
        if   event.code == BTN_A:
            if (distanceRightSensor()) > 30:
                print('Right')
                right()
            else:
                print ('Object @ R')
                stop()
        #LEFT
        if   event.code == BTN_X:
            if (distanceLeftSensor()) > 30:
                print('Left')
                left()
            else:
                print ('Object @ L')
                stop()
        #Unimportant
        if   event.code == BTN_START:
                print('Maybe...')
                GPIO.output(A1, 1) #A1
                GPIO.output(A2, 1) #A2
                GPIO.output(B1, 1) #B1
                GPIO.output(B2, 1) #B2
                GPIO.output(C1, 1) #C1
                GPIO.output(C2, 1) #C2
                GPIO.output(D1, 1) #D1
                GPIO.output(D2, 1) #D2
                sleep(.055)
                stop()
    else:
        stop()
           
