import tkinter as tk
from tkinter import ttk

window = tk.Tk()    
window.title("체크 버튼 1")

label1 = ttk.Label(window, text="취미를 선택하세요(여러개 가능)")
label1.grid(row=0, column=0, columnspan=3)

check1 = tk.Checkbutton(window, text="등산")
check1.grid(row=1, column=0)
check1.select()
check2 = tk.Checkbutton(window, text="낚시", state="disabled")
check2.grid(row=1, column=1)
check2.deselect()
check2 = tk.Checkbutton(window, text="독서")
check2.grid(row=1, column=2)

window.mainloop()