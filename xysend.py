import pyautogui as ag
import time

with open('xy.txt', 'a') as File:
    while True:
        File.write("\n")
        xy = str(ag.position())
        File.write(xy) #파일 쓸때 무조건~~~~~ str ㄱㄱ
        time.sleep(2)