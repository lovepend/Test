import pyautogui as pag
import time

# pag.click(486,68)
# time.sleep(0.2)
# pag.mouseUp(487,68)
# time.sleep(1)
# pag.mouseDown(618,219)
# time.sleep(0.2)
# pag.click(618,219, button='left')
# time.sleep(0.2)
# pag.mouseDown(621,221)


import win32api
import win32con


def mouse_click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


# mouse_click(486,68)
# time.sleep(1)
# mouse_click(618,219)


# mouse.click(486,68)