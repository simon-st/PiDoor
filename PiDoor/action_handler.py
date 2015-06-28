
from PiDoor.exceptions import ActionNotFoundException
from PiDoor import pi_handler

def init():
    print('init()')
    lockDoor()
    turnLightOff(1)
    turnLightOff(2)
    startMotionDetection()

def shutdown():
    print('shutdown()')
    stopMotionDetection()
    pi_handler.cleanup()

def handle(action, args):
    print('handle() ... ' +action)
    method = actions.get(action, None)
    if not method is None:
        return method(args)
    else:
        raise ActionNotFoundException(action)

def unlockDoor():
    print('unlockDoor()')
    pi_handler.unlockDoor()
    return 'Success'

def lockDoor():
    print('lockDoor()')
    pi_handler.lockDoor()
    return 'Success'

def door(args):
    action = args['action']
    if action == 'lock':
        lockDoor()
    elif action == 'unlock':
        unlockDoor()
    else:
        raise ActionNotFoundException(action)

def turnLightOn(index):
    print('turnLightOn()')
    pi_handler.turnOnLight(index)
    return 'Success'

def turnLightOff(index):
    print('turnLightOff()')
    pi_handler.turnOffLight(index)
    return 'Success'

def lights(args):
    action = args['action']
    index = args['index']
    if action == 'on':
        turnLightOn(index)
    elif action == 'off':
        turnLightOff(index)
    else:
        raise ActionNotFoundException(action)
    
def startMotionDetection():
    print('startMotionDetection()')
    pi_handler.startMotionDetection()

def stopMotionDetection():
    print('stopMotionDetection()')
    pi_handler.stopMotionDetection()
    
actions = {
    'door' : door,
    'lights' : lights
}