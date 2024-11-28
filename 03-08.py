import tkinter as tk

window = tk.Tk()    
window.title("버튼1")

button1 = tk.Button(window, text='여기를 클릭', fg='red')
button1.pack()

window.mainloop()