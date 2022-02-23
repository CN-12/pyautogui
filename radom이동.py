import random as rd
import pyautogui as ag

while True:
    ag.moveTo(rd.randint(1, 1000), rd.randint(1, 1000), 0.5)
    #하지 마세요 경고 