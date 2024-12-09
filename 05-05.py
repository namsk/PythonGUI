import tkinter as tk
from tkinter import ttk

window = tk.Tk()    
window.title("위젯 크기 설정")

# ttk는 width, height 옵션을 지원하지 않음
button1 = tk.Button(window, text="버튼1", height=10, width=30)
button2 = tk.Button(window, text="버튼2", height=10, width=30)
button3 = tk.Button(window, text="버튼3", height=10, width=30)

button1.pack(side=tk.LEFT)
button2.pack(side=tk.LEFT)
button3.pack(side=tk.LEFT)

window.mainloop()