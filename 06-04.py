import tkinter as tk
from tkinter import messagebox

def enterMouse(event):
    photo = tk.PhotoImage(file="gif/cat_image.gif")
    label1.configure(image=photo)
    label1.image = photo

def leaveMouse(event):
    photo = tk.PhotoImage(file="gif/fox_image.gif")
    label1.configure(image=photo)
    label1.image = photo

window = tk.Tk()    
window.title("마우스 이벤트 3")
window.geometry("800x800")

photo = tk.PhotoImage(file="gif/dog_image.gif")
label1 = tk.Label(window, image=photo)
label1.pack(expand=1, anchor=tk.CENTER)

label1.bind("<Enter>", enterMouse)
label1.bind("<Leave>", leaveMouse)

window.mainloop()