import tkinter as tk
from tkinter import ttk

def click_button():
    result = intValue1.get() + intValue2.get()
    label2.configure(text="결과: " + str(result))
    
window = tk.Tk()    
window.title("덧셈 계산기")

intValue1 = tk.IntVar()
intValue2 = tk.IntVar()

label1 = ttk.Label(window, text="더할 숫자를 입력하세요").grid(row=0, column=0)
entry1 = ttk.Entry(window, width=15, textvariable=intValue1).grid(row=1, column=0)
entry2 = ttk.Entry(window, width=15, textvariable=intValue2).grid(row=1, column=1)
button1 = ttk.Button(window, text="덧셈 계산", command=click_button).grid(row=2, column=0)

# label2는 외부에서 configure로 접근해야 하기 때문에 grid를 별도 라인에 작성해야 함
label2 = ttk.Label(window, text="결과:", foreground="red")
label2.grid(row=3, column=0)

window.mainloop()