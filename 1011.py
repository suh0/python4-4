from tkinter import *


btnList=[None]*9
fnameList=["dog.gif","1.gif", "2.gif","3.gif", "4.gif","5.gif","6.gif","7.gif","8.gif"]
photoList=[None]*9
i, k=0,0
xPos,yPos=0,0
num=0

window =Tk()
window.geometry("210x210")

for i in range(0,9):
    photoList[i]=PhotoImage(file="gif/"+fnameList[i])
    btnList[i]=Button(window,image=photoList[i])

for i in range(0,3):
    for k in range(0,3):
        btnList[num].place(x=xPos, y=yPos)
        num+=1
        xPos += 70
    xPos=0
    yPos+=70

window.mainloop()