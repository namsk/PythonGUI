import tkinter as tk

window = tk.Tk()    
window.title("레이블4")

photo1 = tk.PhotoImage(file="gif/emu-14760_256.gif")
photo2 = tk.PhotoImage(file="gif/pixel-art-13575_256.gif")
photoLabel1 = tk.Label(window, image=photo1)
photoLabel2 = tk.Label(window, image=photo2) 

photoLabel1.pack()
photoLabel2.pack()

window.mainloop()