import tkinter as tk

window = tk.Tk()    
window.title("파이썬 GUI 연습")
window.geometry("500x300")  # 윈도우의 기본 크기 지정
window.resizable(width=True, height=False)  # 가로폭만 사이즈 조절을 허용함

window.mainloop()