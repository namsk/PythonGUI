import tkinter as tk
from tkinter import ttk

def check_button():
    if (chkValue1.get() == 0):
        label1.configure(text="Off : 꺼짐", foreground="blue")
    else:
        label1.configure(text="On : 켜짐", foreground="red")

window = tk.Tk()    
window.title("체크 버튼 2")

label1 = ttk.Label(window, width=15, text="여기가 바뀜")
label1.grid(row=0, column=0)

chkValue1 = tk.IntVar()
# check를 켜면 1, 끄면 0
check1 = ttk.Checkbutton(window, text="클릭하세요", variable=chkValue1, command=check_button)
check1.grid(row=0, column=1)

window.mainloop()