from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con

# left X370 Y600
# left-center X430 Y600
# right-center X500 Y600
# right X570 Y600

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01) #Pauses script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def main():
    while keyboard.is_pressed('q') == False:
        if pyautogui.pixel(370, 300)[0] == 0:
            click(370, 300)
        if pyautogui.pixel(430, 300)[0] == 0:
            click(430, 300)
        if pyautogui.pixel(500, 300)[0] == 0:
            click(500, 300)
        if pyautogui.pixel(570, 300)[0] == 0:
            click(570, 300)

if __name__ == '__main__':
    main()
