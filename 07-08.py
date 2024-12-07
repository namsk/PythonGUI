import tkinter as tk


def pressKey(event):
    global curX, curY
    key = event.keycode
    if key == 37:
        curX -= 10
    elif key == 38:
        curY -= 10
    elif key == 39:
        curX += 10
    elif key == 40:
        curY += 10

    label.place(x=curX, y=curY)


window = tk.Tk()
window.title("특수키 이벤트 2")
window.geometry("400x400")

curX, curY = 100, 100

photo = tk.PhotoImage(file="gifs/fox.gif")
label = tk.Label(window, image=photo, width=150, height=150)
label.place(x=curX, y=curY)

window.bind("<Up>", pressKey)
window.bind("<Down>", pressKey)
window.bind("<Left>", pressKey)
window.bind("<Right>", pressKey)

window.mainloop()
