import tkinter as tk

window = tk.Tk()    
window.title("레이블3")

photo = tk.PhotoImage(file="gif/emu-14760_256.gif")
photoLabel = tk.Label(window, image=photo) 
# 텍스트 옵션과 image 옵션이 같이 오면 image 옵션이 우선

photoLabel.pack()

window.mainloop()