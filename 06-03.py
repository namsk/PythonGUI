import tkinter as tk
from tkinter import messagebox

def clickMouse(event):
    messagebox.showinfo("마우스", "그림에서 마우스가 클릭됨")

window = tk.Tk()    
window.title("마우스 이벤트 3")
window.geometry("800x800")

photo = tk.PhotoImage(file="gif/dog_image.gif")
label1 = tk.Label(window, image=photo)
label1.pack(expand=1, anchor=tk.CENTER)

label1.bind("<Button>", clickMouse)

window.mainloop()