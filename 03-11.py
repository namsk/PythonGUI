import tkinter as tk

def click_button():
    label1.configure(font=('궁서체', 40))
    label1.configure(text="버튼 누름")
    label1.configure(fg="red")

    button1.configure(state="disabled")

window = tk.Tk()    
window.title("버튼4")
window.geometry("300x200")

label1 = tk.Label(window, text="이 글자가 바뀝니다.")
label1.pack()
button1 = tk.Button(window, text="여기를 클릭", command=click_button)
button1.pack()

window.mainloop()