import sys
import tkinter as tt
from tkinter import ttk
from datetime import date

tk = tt.Tk()

#윈도우 창 설정
tk.title('picture_division') #창 제목
tk.geometry('470x220+550+300') #위치

# 사이즈 조절 가능 여부 설정 (세로, 가로)
tk.resizable(True, True)  # (세로 고정, 가로 조절 가능)

# 날짜 작성
date = ttk.Label(tk, anchor='w', text='Today: %s' % date.today().strftime('%x'))
date.pack(fill='x', side='bottom')

# 레이블 추가
a_label = ttk.Label(tk)
a_label.pack(side='bottom', anchor='s')

a_label2 = ttk.Label(tk)
a_label2.pack(side='bottom', anchor='s')

'''
# 텍스트 박스 추가
name = tt.StringVar()
name_entered = ttk.Entry(tk, width=12, textvariable=name)
name_entered.pack(side='bottom', anchor='y')
'''

# 버튼 클릭 함수
def click_start():
    a_label.configure(command= aa.py)  # 버튼 누르면 창 연동..하고싶음.
    a_label.configure(foreground='red')  # 버튼 누르면 바뀌는 레이블 값의 색
#    action.configure(command= aa.py)  # name.get() : 텍스트박스에 입력한 값

def click_end():
    tk.quit()

# 버튼 추가
action = ttk.Button(tk, text="시작", command=click_start)
action.pack(side='bottom', anchor='s')

action1 = ttk.Button(tk, text="종료", command=click_end)
action1.pack(side='bottom', anchor='s')

# 실행
tk.mainloop()