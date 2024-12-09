import tkinter as tk
from tkinter import messagebox

def click_button():
    messagebox.showinfo("이미지 버튼 누름", "사진이 바뀝니다.")
    photo = tk.PhotoImage(file="gif/pixel-art-13575_256.gif")
    button1.configure(image=photo)
    button1.image=photo

window = tk.Tk()    
window.title("버튼5")

photo = tk.PhotoImage(file="gif/emu-14760_256.gif")
button1 = tk.Button(window, image=photo, command=click_button)
button1.pack()

window.mainloop()