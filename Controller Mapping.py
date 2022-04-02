#import evdev
from evdev import InputDevice,categorize, ecodes

gamepad = InputDevice('/dev/input/event8')

print(gamepad)

for event in gamepad.read_loop():
    print(categorize(event))
    
#When you run this it will tell you all the input and output shit for the controller. I also put images in the drive with it all