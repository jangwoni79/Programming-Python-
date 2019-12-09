import pyautogui as pag
import time


if __name__ == '__main__':
    #메모장 프로그램 실행
    pag.moveTo(91, 1053)
    pag.click()
    pag.moveTo(128, 1020)
    pag.typewrite("notepad")
    time.sleep(1)
    pag.press("enter")
    time.sleep(1)
    pag.moveTo(1128, 385)
    pag.click()
    pag.typewrite("hello world!")
    pag.press("hangul")
    pag.press("enter")
    pag.press("enter")
    pag.typewrite("qksrkqrnsk tptkddk!")
    pag.hotkey('ctrl', 's')
    pag.typewrite("C:\\Users\\")
    pag.press("hangul")
    pag.typewrite("wkddnjsdl")
    pag.press("hangul")
    pag.typewrite("\\Desktop\\")
    pag.press("hangul")
    pag.typewrite("vkdlTJs dnjfem")
    pag.press("enter")
    #hello world 치기
    #두 번 내리기
    #반갑구나 세상아 치기
    #저장
    #파일 이름 : 파이썬 월드