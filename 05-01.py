import tkinter as tk
from tkinter import ttk

window = tk.Tk()    
window.title("수평 정렬")

button1 = ttk.Button(window, text="버튼1")
button2 = ttk.Button(window, text="버튼2")
button3 = ttk.Button(window, text="버튼3")

# button1.pack(side = tk.LEFT)
# button2.pack(side = tk.LEFT)
# button3.pack(side = tk.LEFT)

button1.pack(side = tk.RIGHT)
button2.pack(side = tk.RIGHT)
button3.pack(side = tk.RIGHT)

window.mainloop()