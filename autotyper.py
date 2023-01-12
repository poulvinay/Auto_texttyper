import pyautogui
import time
text=str(input("Enter text that you what to type continuously: "))
counter = int(input("Enter how many times you what to type the text: "))
while counter>0:
    time.sleep(1)
    pyautogui.typewrite(text)
    time.sleep(0.5)
    pyautogui.press('enter')
    counter -=1
