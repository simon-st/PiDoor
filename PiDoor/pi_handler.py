
from PiDoor.config import *
from PiDoor.exceptions import LightIndexNotFoundException
import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)

GPIO.setup(GPIO_PIN_SERVO,GPIO.OUT)
GPIO.setup(GPIO_PIN_RELY_1,GPIO.OUT)
GPIO.setup(GPIO_PIN_RELY_2,GPIO.OUT)
GPIO.setup(GPIO_MOTION,GPIO.IN)

servo = GPIO.PWM(GPIO_PIN_SERVO,50)
servo.start(SERVO_POS_RIGHT)
motion_detection_on = True
    
def cleanup():
    servo.stop()
    GPIO.cleanup()

def moveServo(pos):
    servo.ChangeDutyCycle(pos)

def unlockDoor():
    print('pi_handler.unlockDoor()')
    moveServo(SERVO_POS_LEFT)

def lockDoor():
    print('pi_handler.lockDoor()')
    moveServo(SERVO_POS_RIGHT)
    
def setLightMode(index, mode):
    if index == 1:
        pin = GPIO_PIN_RELY_1
    elif index == 2:
        pin = GPIO_PIN_RELY_2
    else:
        raise LightIndexNotFoundException(index)
    
    GPIO.output(pin, mode)
    
def turnOnLight(index):
    print('pi_handler.turnOnLight()')
    setLightMode(index, GPIO.LOW)

def turnOffLight(index):
    print('pi_handler.turnOffLight()')
    setLightMode(index, GPIO.HIGH)

def startMotionDetection(callback=None):
    global motion_detection_on
    motion_detection_on = True
    has_motion = False
    print('start detection loop')
    while motion_detection_on:
        motion = GPIO.input(GPIO_MOTION)
        if not motion == has_motion:
            has_motion = motion
            if motion:
                print('motion')
                callback(True)
            else:
                print('no motion')
                callback(False)
        time.sleep(1)
    
    print('stop detection loop')

def stopMotionDetection():
    global motion_detection_on
    motion_detection_on = False

def isDark():
    return getLightIndex() >= LIGHT_SENSOR_DARK_INDEX

def getLightIndex():
    GPIO.setup(GPIO_LIGHT_SENSOR, GPIO.OUT)
    GPIO.output(GPIO_LIGHT_SENSOR, GPIO.LOW)
    time.sleep(0.1)
    
    index = 0
    GPIO.setup(GPIO_LIGHT_SENSOR, GPIO.IN)
    while GPIO.input(GPIO_LIGHT_SENSOR) == GPIO.LOW:
        index += 1
    
    print('getLightIndex() ... index: ' +str(index))
    
    return index
    
    