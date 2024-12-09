import tkinter as tk

window = tk.Tk()    
window.title("레이블1")

label1 = tk.Label(window, text="Python~~ GUI를")
label1.pack()   # 만들어진 컨트롤을 화면에 표시

window.mainloop()