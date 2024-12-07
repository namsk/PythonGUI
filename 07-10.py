import tkinter as tk


def pressKey(event):
    global x1, y1, x2, y2
    key = event.keycode
    if key == 37:
        x2 = x1 - 10
    elif key == 38:
        y2 = y1 - 10
    elif key == 39:
        x2 = x1 + 10
    elif key == 40:
        y2 = y1 + 10

    canvas.create_line(x1, y1, x2, y2, fill="black")
    x1, y1 = x2, y2


x1, y1, x2, y2 = 200, 200, 200, 200
window = tk.Tk()
window.title("특수키 이벤트 4")
window.geometry("400x400")

canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

window.bind("<Key>", pressKey)
window.mainloop()
