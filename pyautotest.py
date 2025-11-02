import pyautogui
import time
import pandas as pd
import keyboard
#move mouse based on csv file
location_data = pd.read_csv('clash coords.csv')
location_data['rgb'] = None  # Create a new column for RGB values
# move mouse to the first location
x = location_data.iloc[0]['x']
y = location_data.iloc[0]['y']
time.sleep(5)  # 5 second delay to allow user to switch to the target application
rgb = pyautogui.screenshot().getpixel((x, y))
pyautogui.moveTo(x, y, duration=0)  # Move to (x, y) over 0.5 seconds
pyautogui.click(button='left')
time.sleep(7)
try:
    for index, row in location_data.iterrows():
        x = row['x']
        y = row['y']
        pyautogui.moveTo(x, y, duration=0)  # Move to (x, y) over 0.5 seconds
        rgb = pyautogui.screenshot().getpixel((x, y))
        print(rgb)
        location_data[index, 'rgb'] = str(rgb)
        time.sleep(.3)  # Pause for a second at each location
except KeyboardInterrupt:
    print('\n')
    print('Exiting...')
    