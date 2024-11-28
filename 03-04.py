import tkinter as tk

window = tk.Tk()    
window.title("레이블2")

label1 = tk.Label(window, text="Python~~ GUI를")
label2 = tk.Label(window, text="수강 중에", font=("궁서체", 40), fg='red')
label3 = tk.Label(window, text="있습니다", bg='yellow', width=20, height=5, anchor=tk.SE)

label1.pack()   
label2.pack()
label3.pack()

window.mainloop()