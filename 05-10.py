import tkinter as tk
from tkinter import ttk
import random
import os

## 변수 선언 부분 ##
btnList = [None] * 9
fnameList = []

# 이미지 파일을 리스트에 추가 #
gif_dir = os.path.join(os.path.dirname(__file__), 'gif')
for filename in os.listdir(gif_dir):
    if filename.endswith('.gif') and '_256x256' in filename:
        # fnameList.append(os.path.join(gif_dir, filename))
        fnameList.append(filename)

random.shuffle(fnameList)
photoList = [None] * 9

i, k = 0, 0
xPos, yPos = 0, 0
num = 0

## 메인 코드 부분 ##
window = tk.Tk()    
window.title("고정 위치 배치 2")
window.geometry("768x768")

for i in range(9):
    photoList[i] = tk.PhotoImage(file="gif/" + fnameList[i])
    btnList[i] = ttk.Button(window, image=photoList[i])

for i in range(3):
    for k in range(3):
        btnList[num].place(x=xPos, y=yPos)
        num += 1

        xPos += 256
    xPos = 0
    yPos += 256

window.mainloop()