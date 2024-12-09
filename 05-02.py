import tkinter as tk
from tkinter import ttk

window = tk.Tk()    
window.title("수직 정렬")

btnList = [None] * 3

for i in range(3):
    btnList[i] = ttk.Button(window, text="버튼" + str(i + 1))

for i in range(3):
    # btnList[i].pack(side=tk.TOP)
    btnList[i].pack(side=tk.BOTTOM)
    
window.mainloop()