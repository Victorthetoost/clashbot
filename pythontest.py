import pyautogui
import time
import keyboard
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        position_str = f'X: {str(x).rjust(4)} Y: {str(y).rjust(4)}'
        print(position_str, end='')
        print('\b' * len(position_str), end='', flush=True)
        time.sleep(0.1) # Optional: add a small delay to reduce CPU usage
        if keyboard.is_pressed('w'):  # If 'q' is pressed, exit the loop
            print(f"(x:{x},y:{y})")
except KeyboardInterrupt:
    print('\n')
    print('Exiting...')