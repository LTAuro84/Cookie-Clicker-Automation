import pyautogui
import keyboard
import time

time.sleep(5)

cookie = pyautogui.locateOnScreen("cookie.png", confidence=0.6)

position = cookie

while True:
    if keyboard.is_pressed("q"):
        break
    pyautogui.click(position)


    if time.time() % 5 < 0.1:

        try:
            cursor = pyautogui.locateOnScreen("cursor_button.png", confidence=0.6)

            if cursor:
                pyautogui.click(cursor)
    
        except:
            pass

        try:
            grandma = pyautogui.locateOnScreen("grandma_button.png", confidence=0.6)

            if grandma:
                pyautogui.click(grandma)
        except:
            pass