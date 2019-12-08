import pyautogui as pag
import time     #sleep

if __name__ == '__main__':
    #time.sleep(2)
    pag.moveTo(200, 200, 2)
    pag.click()
    pag.typewrite("happy birㅎㅈthday to seungweon!", interval=0.2)
    pag.press("enter")
    pag.typewrite("happy birthday to namkyeoung!")
    pag.press("hangul")
    pag.typewrite("skaruddk toddlf cnrgkgo!!!")