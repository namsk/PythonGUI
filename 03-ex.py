import tkinter as tk
def click_prev():
    global index
    index -=1
    if (index < 0): # 인덱스가 -1이면 마지막 사진으로
        index = len(fileList) - 1
    photo = tk.PhotoImage(file = fileList[index])
    imageLabel.configure(image=photo)
    imageLabel.image = photo

def click_next():
    global index
    index += 1
    if (index >= len(fileList)):
        index = 0
    photo = tk.PhotoImage(file = fileList[index])
    imageLabel.configure(image=photo)
    imageLabel.image = photo

fileList = ["gif/pixel-art-13575_256.gif", "gif/hamster-14608_256.gif", "gif/emu-14760_256.gif", "gif/robot-4212_256.gif"]
index = 0

window = tk.Tk()
window.title("3장 적용하기")

btnPrev = tk.Button(window, text="<< Prev", command=click_prev)
btnPrev.pack()
btnNext = tk.Button(window, text="Next >>", command=click_next)
btnNext.pack()

photo = tk.PhotoImage(file=fileList[index])
imageLabel = tk.Label(window, image = photo)
imageLabel.pack()

window.mainloop()