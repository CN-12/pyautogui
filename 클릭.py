import pyautogui as ag
import time

time.sleep(0.5)
ag.click() #기본값은 좌클릭
ag.click(button="right") #이렇게 해주면 이제 우클릭
ag.doubleClick() #무조건 대문자 주의하고 이렇게 해주면 더블클릭 ㅇㅋ?
ag.click(clicks=3, interval=1) #3번 클릭 1초마다 