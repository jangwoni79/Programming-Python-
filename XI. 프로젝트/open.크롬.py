import pyautogui as pag
import time

if __name__ == '__main__':
    # #크롬 이미지 인식
    # #center = pag.locationOnScreen("크롬아이콘.PNG")
    # data = pag.locateOnScreen("크롬아이콘.PNG")
    # print(data)
    # #가운데 좌표 찾기
    # center = pag.center(data)
    # #마우스 이동
    # # pag.moveTo(center, duration=2)
    # #더블 클릭
    # pag.doubleClick(center, duration=2)

    data = pag.locateAllOnScreen("크롬아이콘.PNG")
    for data in data:
        center = pag.center(data)
        pag.moveTo(center, duration = 0.2)