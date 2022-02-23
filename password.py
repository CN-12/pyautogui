import pyautogui as ag

a = ag.password(text="내용입니다", title="제목입니다", default="입력하세요", mask="*")
print(a)