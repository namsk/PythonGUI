import tkinter as tk
from tkinter.colorchooser import askcolor

def clickButton():
    global penColor
    color = askcolor()
    penColor = color[1]


def mouseDown(event):
    global x1, y1, x2, y2
    x1, y1 = event.x, event.y
    
def leftMouseDrop(event):
    global x1, y1, x2, y2, penColor
    x2, y2 = event.x, event.y
    if (x1 > x2):
        x1, x2 = x2, x1
    if (y1 > y2):
        y1, y2 = y2, y1

    canvas.create_line(x1, y1, x2, y2, fill=penColor)

def middleMouseDrop(event):
    global x1, y1, x2, y2, penColor
    x2, y2 = event.x, event.y

    canvas.create_oval(x1, y1, x2, y2, fill=penColor)


def rightMouseDrop(event):
    global x1, y1, x2, y2, penColor
    x2, y2 = event.x, event.y
    if (x1 > x2):
        x1, x2 = x2, x1
    if (y1 > y2):
        y1, y2 = y2, y1

    canvas.create_line(x1, y1, x1, y2, x2, y2, x2, y1, x1, y1, fill=penColor)

x1, y1, x2, y2 = 0, 0, 0, 0
penColor = None

window = tk.Tk()    
window.title("6장 적용하기")
window.geometry("400x400")

button1 = tk.Button(window, text="색상 선택", command=clickButton)
button1.pack()

canvas = tk.Canvas(window, height=400, width=400)
canvas.bind("<Button-1>", mouseDown)
canvas.bind("<ButtonRelease-1>", leftMouseDrop)
canvas.bind("<Button-2>", mouseDown)
canvas.bind("<ButtonRelease-2>", middleMouseDrop)
canvas.bind("<Button-3>", mouseDown)
canvas.bind("<ButtonRelease-3>", rightMouseDrop)
canvas.pack()

window.mainloop()