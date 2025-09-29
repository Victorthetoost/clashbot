import pyautogui
import time
import pandas as pd
#1,859,1051,199,80,203
#2,903,1051,178,74,182
#3,946,1052,164,36,168
#4,985,1053,184,30,190
#5,1029,1054,184,30,190
#6,1070,1053,184,30,190
#7,1114,1053,184,30,190
#8,1154,1052,186,37,191
#9,1197,1053,179,24,185
#10,1235,1054,109,115,212
#sadjfhaslkdjfhaslkdjfhklaj
try:
    while True:
        time.sleep(1)
        pyautogui.moveTo(901,322, duration=0) 
        if pyautogui.pixel(901,322) == (224, 62, 145):
            print("tower lost detected")
        if pyautogui.pixel(1235,1054) == (109,115,212):
            print("you have 10 elixir")
        elif pyautogui.pixel(1197,1053) == (179,24,185):
            print("you have 9 elixir")
        elif pyautogui.pixel(1154,1052) == (186,37,191):
            print("you have 8 elixir")
        elif pyautogui.pixel(1114,1053) == (184,30,190):
            print("you have 7 elixir")
        elif pyautogui.pixel(1070,1053) == (184,30,190):
            print("you have 6 elixir")
        elif pyautogui.pixel(1029,1054) == (184,30,190):
            print("you have 5 elixir")
        elif pyautogui.pixel(985,1053) == (184,30,190):
            print("you have 4 elixir")
        elif pyautogui.pixel(946,1052) == (164,36,168):
            print("you have 3 elixir")
        elif pyautogui.pixel(903,1051) == (178,74,182):
            print("you have 2 elixir")
        elif pyautogui.pixel(859,1051) == (199,80,203):
            print("you have 1 elixir")
except KeyboardInterrupt:
    print('\n')
    print('Exiting...')