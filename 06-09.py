import tkinter as tk
from tkinter.colorchooser import askcolor

def clickButton():
    global penColor
    color = askcolor()
    penColor = color[1]


def mouseDown(event):
    global x1, y1, x2, y2
    x1, y1 = event.x, event.y
    

def mouseDrop(event):
    global x1, y1, x2, y2, penColor
    x2, y2 = event.x, event.y

    print(penColor)

    canvas.create_line(x1, y1, x2, y2, fill=penColor)

x1, y1, x2, y2 = 0, 0, 0, 0
penColor = None

window = tk.Tk()    
window.title("마우스 고급 이벤트 5")
window.geometry("400x400")

button1 = tk.Button(window, text="색상 선택", command=clickButton)
button1.pack()

canvas = tk.Canvas(window, height=400, width=400)
canvas.bind("<Button-1>", mouseDown)
canvas.bind("<ButtonRelease-1>", mouseDrop)
canvas.pack()

window.mainloop()