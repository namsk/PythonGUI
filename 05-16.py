import tkinter as tk
from tkinter import ttk

window = tk.Tk()    
window.title("탭 위젯 2")

tabControl = ttk.Notebook(window)

tabDog = ttk.Frame(tabControl)
tabControl.add(tabDog, text="강아지")
tabCat = ttk.Frame(tabControl)
tabControl.add(tabCat, text="고양이")
tabFox = ttk.Frame(tabControl)
tabControl.add(tabFox, text="여우")

tabControl.pack(expand=1, fill="both")

photoDog = tk.PhotoImage(file="gif/dog_image.gif")
labelDog = tk.Label(tabDog, image=photoDog)
labelDog.pack()

photoCat = tk.PhotoImage(file="gif/cat_image.gif")
labelCat = tk.Label(tabCat, image=photoCat)
labelCat.pack()

photoFox = tk.PhotoImage(file="gif/fox_image.gif")
labelFox = tk.Label(tabFox, image=photoFox)
labelFox.pack()

window.mainloop()