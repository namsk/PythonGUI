import tkinter as tk
from tkinter import ttk

window = tk.Tk()    
window.title("여백 조절 3")

button1 = ttk.Button(window, text="버튼1")
button2 = ttk.Button(window, text="버튼2")
button3 = ttk.Button(window, text="버튼3")

button1.pack(padx=10, pady=10, ipadx=10, ipady=10)
button2.pack(padx=10, pady=10, ipadx=10, ipady=10)
button3.pack(padx=10, pady=10, ipadx=10, ipady=10)

window.mainloop()