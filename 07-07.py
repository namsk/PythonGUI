import tkinter as tk


def pressKey(event):
    key = event.keycode
    txt = "Shift + " + str(key)
    label1.configure(text=txt)


window = tk.Tk()
window.title("특수키 이벤트 1")
window.geometry("150x150")

label1 = tk.Label(window, text="", font=('맑은고딕', 15))
label1.pack(expand=1, anchor=tk.CENTER, side=tk.TOP)

window.bind("<Shift-Up>", pressKey)
window.bind("<Shift-Down>", pressKey)
window.bind("<Shift-Left>", pressKey)
window.bind("<Shift-Right>", pressKey)

window.mainloop()
