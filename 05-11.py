import tkinter as tk
from tkinter import ttk

window = tk.Tk()    
window.title("레이블 프레임 1")

frame1 = ttk.LabelFrame(window, text="레이블 프레임")
frame1.grid(row=0, column=0, padx=10, pady=1)

button1 = ttk.Button(frame1, text="버튼1").grid(row=0, column=0)
button2 = ttk.Button(frame1, text="버튼2").grid(row=0, column=1)
button3 = ttk.Button(frame1, text="버튼3").grid(row=0, column=2)

for widget in frame1.winfo_children():
    widget.grid_configure(padx=10, pady=10)
    
window.mainloop()