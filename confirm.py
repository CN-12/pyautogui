import pyautogui as ag

a = ag.confirm(text="내용입니다", title="제목입니다", buttons=["OK", "Cancel"])
print(a)