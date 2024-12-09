import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def clickLeft(event):
    messagebox.showinfo("마우스", "마우스 왼쪽 버튼 클릭!")

window = tk.Tk()    
window.title("마우스 이벤트 1")

window.bind("<Button-1>", clickLeft) # 왼쪽 버튼 클릭시 이벤트를 바인딩


window.mainloop()