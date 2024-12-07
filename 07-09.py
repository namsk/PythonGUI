import tkinter as tk
import random


def pressKey(event):
    global penColor
    keycode = event.keycode
    colorList = ["black", "red", "green", "blue", "yellow", "magenta", "cyan"]
    if 112 <= keycode <= 123:
        penColor = colorList[(keycode - 112) % len(colorList)]
    if keycode == 9:
        penColor = random.choice(colorList)


def mouseDown(event):
    global x1, y1, x2, y2
    x1, y1 = event.x, event.y


def mouseDrop(event):
    global x1, y1, x2, y2, penColor
    x2, y2 = event.x, event.y
    canvas.create_line(x1, y1, x2, y2, fill=penColor)


x1, y1, x2, y2 = 0, 0, 0, 0
penColor = "black"

window = tk.Tk()
window.title("특수키 이벤트 3")
window.geometry("400x400")

canvas = tk.Canvas(window, width=400, height=400)
canvas.bind("<Button-1>", mouseDown)
canvas.bind("<ButtonRelease-1>", mouseDrop)
canvas.pack()

window.bind("<Key>", pressKey)
window.mainloop()
