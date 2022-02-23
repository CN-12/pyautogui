import pyautogui as ag
import time
import pyperclip as  pc
time.sleep(1)
ag.write("hello", interval=0.25) #0.25초씩, 영어만 되가지고 한글 쓸려면 pyperclip 사용해서 복붙해야함 
pc.copy("엄준식")
ag.hotkey("ctrl", "v")
