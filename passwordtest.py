import pyautogui as ag

a = ag.password(text="엄준식이라고합니다", title="엄준식", default="입력해주세엄",mask="엄")
print(a)