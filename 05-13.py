import tkinter as tk
from tkinter import ttk

window = tk.Tk()  
window.title("레이블 프레임 3")

frame1 = ttk.LabelFrame(window, text="부모 프레임")
frame1.grid(row=0, column=0, padx=10, pady=10)

button1 = ttk.Button(frame1, text="버튼1").grid(row=0, column=0)
button2 = ttk.Button(frame1, text="버튼2").grid(row=0, column=1)
button3 = ttk.Button(frame1, text="버튼3").grid(row=0, column=2)

subframe1 = ttk.LabelFrame(frame1, text="자식 프레임 1")
subframe1.grid(row=1, column=0, padx=10, pady=10)

label1 = ttk.Label(subframe1, text="레이블1").grid(row=0, column=0)
label2 = ttk.Label(subframe1, text="레이블2").grid(row=0, column=1)

subframe2 = ttk.LabelFrame(frame1, text="자식 프레임 2")
subframe2.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

radio1 = ttk.Radiobutton(subframe2, text="라디오1").grid(row=0, column=0)
radio2 = ttk.Radiobutton(subframe2, text="라디오2").grid(row=0, column=1)
radio3 = ttk.Radiobutton(subframe2, text="라디오3").grid(row=0, column=2)

window.mainloop()