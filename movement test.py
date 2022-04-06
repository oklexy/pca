#Controlling the PCA: https://pypi.org/project/joycon-python/
import RPi.GPIO as GPIO
import time
import sys

from evdev import InputDevice, categorize, ecodes


#creates object 'gamepad' to store the data
gamepad = InputDevice('/dev/input/event8')

#button code variables (PLEASE CHECK AND CHANGE WHAT IS WRITE AND WHAT ISNT)
BTN_B = 305          #Actually the X Button
BTN_A = 304          #Actually the A button
BTN_C = 306          #Actually the B button
BTN_X = 307          #Actually the Y button

# Setup of GPIO pin numbering type
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Assign the pin numberings for the motors
Motor_A1 = 21
Motor_A2 = 26
Motor_B1 = 19
Motor_B2 = 24
Motor_C1 = 11
Motor_C2 = 15
Motor_D1 = 22
Motor_D2 = 12
# Sensor_FL = 5
# Sensor_FR = 8
# Sensor_RF = 13
# Sensor_RB = 16
# Sensor_BR = 10
# Sensor_BL = 18
# Sensor_LB = 23
# Sensor_LF = 7

# Set the GPIO pins to be output in nature
GPIO.setup(Motor_A1, GPIO.OUT)
GPIO.setup(Motor_A2, GPIO.OUT)
GPIO.setup(Motor_B1, GPIO.OUT)
GPIO.setup(Motor_B2, GPIO.OUT)
GPIO.setup(Motor_C1, GPIO.OUT)
GPIO.setup(Motor_C2, GPIO.OUT)
GPIO.setup(Motor_D1, GPIO.OUT)
GPIO.setup(Motor_D2, GPIO.OUT)

#The setup for all the sensors
# GPIO.setup(Sensor_FL, GPIO.IN)      #GPIO ->Front Left Sensor 
# GPIO.setup(Sensor_FR, GPIO.IN)      #GPIO ->Front Right Sensor 
# GPIO.setup(Sensor_RF, GPIO.IN)      #GPIO ->Right Front Sensor 
# GPIO.setup(Sensor_RB, GPIO.IN)      #GPIO ->Right Back Sensor 
# GPIO.setup(Sensor_BR, GPIO.IN)		#GPIO ->Back Right Sensor 
# GPIO.setup(Sensor_BL, GPIO.IN)		#GPIO ->Back Left Sensor 
# GPIO.setup(Sensor_LB, GPIO.IN)		#GPIO ->Left Back Sensor 
# GPIO.setup(Sensor_LF, GPIO.IN)		#GPIO ->Left Front Sensor

#In hignsight a possibly uneeded set of code but it should be fine
# SensorFrontLeft = GPIO.input(Sensor_FL)
# SensorFrontRight = GPIO.input(Sensor_FR)
# SensorRightFront = GPIO.input(Sensor_RF)
# SensorRightBack = GPIO.input(Sensor_RB)
# SensorBackRight = GPIO.input(Sensor_BR)
# SensorBackLeft = GPIO.input(Sensor_BL)
# SensorLeftBack = GPIO.input(Sensor_LB)
# SensorLeftFront = GPIO.input(Sensor_LF)
# 
# Initiation time
time.sleep(2)

# Creating the different movement functions
# Both motors moving forward

def move_forward():    
    GPIO.output(Motor_A1, GPIO.HIGH)
    GPIO.output(Motor_A2, GPIO.LOW)
    GPIO.output(Motor_B1, GPIO.HIGH)
    GPIO.output(Motor_B2, GPIO.LOW)
    GPIO.output(Motor_C1, GPIO.HIGH)
    GPIO.output(Motor_C2, GPIO.LOW)
    GPIO.output(Motor_D1, GPIO.HIGH)
    GPIO.output(Motor_D2, GPIO.LOW)

def move_backwards():
    GPIO.output(Motor_A1, 0)
    GPIO.output(Motor_A2, 1)
    GPIO.output(Motor_B1, 0)
    GPIO.output(Motor_B2, 1)
    GPIO.output(Motor_C1, 0)
    GPIO.output(Motor_C2, 1)
    GPIO.output(Motor_D1, 0)
    GPIO.output(Motor_D2, 1)

def turn_right():
    GPIO.output(Motor_A1, 1)
    GPIO.output(Motor_A2, 0)
    GPIO.output(Motor_B1, 0)
    GPIO.output(Motor_B2, 1)
    GPIO.output(Motor_C1, 1)
    GPIO.output(Motor_C2, 0)
    GPIO.output(Motor_D1, 0)
    GPIO.output(Motor_D2, 1)

def turn_left():
    GPIO.output(Motor_A1, 0)
    GPIO.output(Motor_A2, 1)
    GPIO.output(Motor_B1, 1)
    GPIO.output(Motor_B2, 0)
    GPIO.output(Motor_C1, 0)
    GPIO.output(Motor_C2, 1)
    GPIO.output(Motor_D1, 1)
    GPIO.output(Motor_D2, 0)
# Both motors off
def no_movement():
    GPIO.output(Motor_A1, 0)
    GPIO.output(Motor_A2, 0)
    GPIO.output(Motor_B1, 0)
    GPIO.output(Motor_B2, 0)
    GPIO.output(Motor_C1, 0)
    GPIO.output(Motor_C2, 0)
    GPIO.output(Motor_D1, 0)
    GPIO.output(Motor_D2, 0)
    
#def on_press():
    #try:
#Loop and filter by event code and print the mapped label
for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.value == 1:
            if event.code == BTN_B:
                print('X')
                move_forward()
                print ("going forward zoom zoom")
            elif event.code == BTN_A:
                print('A')
                turn_right()
                print ("right turn zoom zoom")
            elif event.code == BTN_C:
                print('B')
                move_backwards()
                print ("going backwards zoom zoom")
            elif event.code == BTN_X:
                print('Y')
                turn_left()
                print ("left turn zoom zoom")                    
      
        else:
            no_movement()
            
# #CURENT IDEA: add all the sensor stuff right under (if event.value ==1;) stuff.
# #Put it down here so we can kill it ezpz
# for event in gamepad.read_loop():
#   if event.type == ecodes.EV_KEY:
#        if event.value == 1:
#            if ((SensorFrontLeft==False) and (SensorLeftFront==False)):
#                print ("Object is on the Front Left corner. ")
#                #Cant go forward or left 
#                if event.code == BTN_A:
#                    print('A')
#                    turn_right()
#                    print ("right turn zoom zoom")
#                elif event.code == BTN_C:
#                    print('B')
#                    move_backwards()
#                    print ("going backwards zoom zoom")
#                else:
#                    no_movement()
# #
# #
#            elif ((SensorFrontRight==False) and (SensorRightFront==False)):
#               print ("Object is on the Front Right corner. ")
#               #Cant go forward or right 
#               if event.code == BTN_C:
#                    print('B')
#                    move_backwards()
#                    print ("going backwards zoom zoom")
#               elif event.code == BTN_X:
#                    print('Y')
#                    turn_left()
#                    print ("left turn zoom zoom")                    
#               else:
#                    no_movement()
# #
# #
#            elif ((SensorRightBack==False) and (SensorBackRight==False)):
#               print ("Object is on the Back Right corner. ")
#               #Cant go backwards or right
#               if event.code == BTN_B:
#                    print('X')
#                    move_forward()
#                    print ("going forward zoom zoom")
#               elif event.code == BTN_X:
#                    print('Y')
#                    turn_left()
#                    print ("left turn zoom zoom")                    
#               else:
#                    no_movement()
# #
# #
#            elif ((SensorBackLeft==False) and (SensorLeftBack==False)):
#               print ("Object is on the Back Left corner. ")
#               #Cant go backwards or left
#               if event.code == BTN_B:
#                    print('X')
#                    move_forward()
#                    print ("going forward zoom zoom")
#               elif event.code == BTN_A:
#                    print('A')
#                    turn_right()
#                    print ("right turn zoom zoom")
#               else:
#                    no_movement()
# #
# #
#            elif ((SensorFrontLeft==False) or (SensorFrontRight==False)):
#               print ("Object is in front. ")
#               #Cant go forward
#               if event.code == BTN_A:
#                    print('A')
#                    turn_right()
#                    print ("right turn zoom zoom")
#               elif event.code == BTN_C:
#                    print('B')
#                    move_backwards()
#                    print ("going backwards zoom zoom")
#               elif event.code == BTN_X:
#                    print('Y')
#                    turn_left()
#                    print ("left turn zoom zoom")                    
#               else:
#                    no_movement()
# #
# #
#            elif ((SensorRightFront==False) or (SensorRightBack==False)):
#               print ("Object is to the right. ")
#               #Cant go right
#               if event.code == BTN_B:
#                    print('X')
#                    move_forward()
#                    print ("going forward zoom zoom")
#               elif event.code == BTN_C:
#                    print('B')
#                    move_backwards()
#                    print ("going backwards zoom zoom")
#               elif event.code == BTN_X:
#                    print('Y')
#                    turn_left()
#                    print ("left turn zoom zoom")                    
#               else:
#                    no_movement()
# #
# #
#            elif ((SensorBackRight==False) or (SensorBackLeft==False)):
#               print ("Object is behind. ")
#               #Cant go backwards
#               if event.code == BTN_B:
#                    print('X')
#                    move_forward()
#                    print ("going forward zoom zoom")
#               elif event.code == BTN_A:
#                    print('A')
#                    turn_right()
#                    print ("right turn zoom zoom")
#               elif event.code == BTN_X:
#                    print('Y')
#                    turn_left()
#                    print ("left turn zoom zoom")                    
#               else:
#                    no_movement()
# #
# #
#            elif ((SensorLeftBack==False) or (SensorLeftFront==False)):
#               print ("Object is to the left. ")
#               #Cant go left
#               if event.code == BTN_B:
#                    print('X')
#                    move_forward()
#                    print ("going forward zoom zoom")
#               elif event.code == BTN_A:
#                    print('A')
#                    turn_right()
#                    print ("right turn zoom zoom")
#               elif event.code == BTN_C:
#                    print('B')
#                    move_backwards()
#                    print ("going backwards zoom zoom")
#               else:
#                    no_movement()
# #
# #
#            else:
#               print ("Nothing around, go crazy. ")
#               if event.code == BTN_B:
#                    print('X')
#                    move_forward()
#                    print ("going forward zoom zoom")
#               elif event.code == BTN_A:
#                    print('A')
#                    turn_right()
#                    print ("right turn zoom zoom")
#               elif event.code == BTN_C:
#                    print('B')
#                    move_backwards()
#                    print ("going backwards zoom zoom")
#               elif event.code == BTN_X:
#                    print('Y')
#                    turn_left()
#                    print ("left turn zoom zoom")                    
#               else:
#                    no_movement()
# #
# #
#     
# ##        KEY = key.char.lower()
# ##        time.sleep(3)
# ##        if KEY in ["w"]:
# ##            move_forward()
# ##        elif KEY in ["a"]:
# ##            turn_left()
# ##        elif KEY in ["s"]:
# ##            move_backwards()
# ##        elif KEY in ["d"]:
# ##            turn_right()
# ##        else:
# ##            no_movement()
# ##    except:
# ##        pass
# 
#on_press()
GPIO.cleanup()