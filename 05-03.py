import tkinter as tk
from tkinter import ttk

window = tk.Tk()    
window.title("폭 조정")

button1 = ttk.Button(window, text="버튼1")
button2 = ttk.Button(window, text="버튼2")
button3 = ttk.Button(window, text="버튼3")

button1.pack(side=tk.TOP, fill=tk.X)    # fill=tk.X 옵션을 추가 -> 버튼의 폭을 윈도우의 폭에 맞춤
button2.pack(side=tk.TOP, fill=tk.X)
button3.pack(side=tk.TOP, fill=tk.X)

window.mainloop()