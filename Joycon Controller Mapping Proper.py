from evdev import InputDevice, categorize, ecodes

print('Joycon R - mapping')

#creates object 'gamepad' to store the data
gamepad = InputDevice('/dev/input/event8')

#button code variables (PLEASE CHECK AND CHANGE WHAT IS WRITE AND WHAT ISNT)
BTN_B = 305          #Actually the X Button
BTN_A = 304          #Actually the A button
BTN_C = 306          #Actually the B button
BTN_X = 307          #Actually the Y button

#Loop and filter by event code and print the mapped label
for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.value == 1:
            if event.code == BTN_B:
                print('X')
            elif event.code == BTN_A:
                print('A')
            elif event.code == BTN_C:
                print('B')
            elif event.code == BTN_X:
                print('Y')
