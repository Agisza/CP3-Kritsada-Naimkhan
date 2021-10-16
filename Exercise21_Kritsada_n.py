from tkinter import *
import math

def leftClickButton(event):
    unit_M = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    if unit_M >30.0 :
        res_Unit = "อ้วนมาก"
    elif unit_M >=25.0 :
        res_Unit = "อ้วน"
    elif unit_M >=23.0 :
        res_Unit = "น้ำหนักเกิน"
    elif unit_M >=18.6 :
        res_Unit = "น้ำหนักปกติ เหมาะสม"
    else:
        res_Unit = "ผอมเกินไป"
    labelResult.configure(text=res_Unit)

MainWindow = Tk()
labelHeight = Label(MainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeigth = Label(MainWindow, text="น้ำหนัก (Kg.)")
labelWeigth.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text = "คำนวน")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2,column=0)
labelResult = Label(MainWindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)


MainWindow.mainloop()