import tkinter as tk
from tkinter import ttk

def click_button():
    exprStr = str(num1.get()) + combo1.get() + str(num2.get())
    resValue = eval(exprStr)
    label2.configure(text=str(resValue))

window = tk.Tk()    
window.title("4장 적용하기")

num1 = tk.IntVar()
num2 = tk.IntVar()

label1 = ttk.Label(window, text="계산할 숫자 및 연산자를 입력하세요", font=("맑은고딕", 16))
label1.grid(row=0, column=0, columnspan=3)
entry1 = ttk.Entry(window, width=10, textvariable=num1).grid(row=1, column=0)

combo1 = ttk.Combobox(window, width=10)
combo1.grid(row=1, column=1)
combo1['values'] = ('+', '-', '*', '/', '%', '**')

entry1 = ttk.Entry(window, width=10, textvariable=num2).grid(row=1, column=2)

button1 = ttk.Button(window, 
                     text="계산하기", 
                     command=click_button)\
            .grid(row=2, column=0, columnspan=3)
label2 = ttk.Label(window, text="결과 :", font=("맑은고딕", 14))
label2.grid(row=3, column=0)

window.mainloop()