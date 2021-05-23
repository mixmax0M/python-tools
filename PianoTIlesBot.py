from pyautogui import *
import win32api, win32con, random, keyboard, time, pyautogui

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01) 
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

# eddot the x and y for your case

while keyboard.is_pressed('s') == False:
    try:
        if pyautogui.pixel(581, 400)[0] == 0:
            click(555, 400)
        if pyautogui.pixel(682, 400)[0] == 0:
            click(666, 400)
        if pyautogui.pixel(770, 400)[0] == 0:
                click(777, 400)
        if pyautogui.pixel(869, 400)[0] == 0:
            click(888, 400)
    except:
        Exception