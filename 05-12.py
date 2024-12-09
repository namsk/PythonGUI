import tkinter as tk
from tkinter import ttk

def click_button():
    if (rdoVar.get() == 1):
        filename = "gif/dog_image.gif"
    elif (rdoVar.get() == 2):
        filename = "gif/cat_image.gif"
    else:
        filename = "gif/fox_image.gif"

    photo = tk.PhotoImage(file=filename)
    imageLabel.configure(image=photo)
    imageLabel.image = photo

window = tk.Tk()    
window.title("레이블 프레임 2")

frame1 = ttk.LabelFrame(window, text="좋아하는 동물은?")
frame1.grid(row=0, column=0, padx=10, pady=10)

rdoVar = tk.IntVar()
radio1 = ttk.Radiobutton(frame1, variable=rdoVar, value=1, text="강아지")
radio1.grid(row=0, column=0)
radio2 = ttk.Radiobutton(frame1, variable=rdoVar, value=2, text="고양이")
radio2.grid(row=0, column=1)
radio3 = ttk.Radiobutton(frame1, variable=rdoVar, value=3, text="여우")
radio3.grid(row=0, column=2)

button1 = ttk.Button(window, text="클릭하세요", command=click_button)
button1.grid(row=1, column=0, columnspan=3)

imageLabel = ttk.Label(window)
imageLabel.grid(row=2, column=0, columnspan=3)

window.mainloop()