import tkinter as tk

window = tk.Tk()    
window.title("버튼2")

button1 = tk.Button(window, text='프로그램 종료', command=quit)
button1.pack()

window.mainloop()