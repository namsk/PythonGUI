import tkinter as tk
from tkinter import ttk

window = tk.Tk()    
window.title("탭 위젯 1")

tabControl = ttk.Notebook(window)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text="탭 1")
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="탭 2")

tabControl.pack(expand=1, # 화면을 꽉 채움
                fill="both", # 화면을 꽉 채움
                padx=10, pady=10)

button1 = tk.Button(tab1, text="버튼1", background='red')   # tab1에 버튼1을 추가
button1.grid(row=0, column=0, padx=50, pady=50)
button2 = tk.Button(tab2, text="버튼2", background='green') # tab2에 버튼2를 추가
button2.grid(row=0, column=0, padx=50, pady=50)

window.mainloop()