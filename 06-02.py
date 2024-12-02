import tkinter as tk
from tkinter import messagebox

def clickButton(event):
    if (event.num == 1): # 왼쪽 버튼
        messagebox.showinfo("마우스", "마우스 왼쪽 버튼 클릭")
    elif (event.num == 2): 
        messagebox.showinfo("마우스", "마우스 가운데 버튼 클릭")
    else:
        messagebox.showinfo("마우스", "마우스 오른쪽 버튼 클릭")

window = tk.Tk()    
window.title("마우스 이벤트 2")

window.bind("<Button>", clickButton) # 모든 버튼 클릭시 이벤트를 바인딩


window.mainloop()