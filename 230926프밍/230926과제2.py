from tkinter import *

fnameList = ["jeju1.gif", "jeju2.gif", "jeju3.gif", "jeju4.gif", "jeju5.gif", "jeju6.gif", "jeju7.gif", "jeju8.gif", "jeju9.gif"]
num = 0
window = Tk()

def ClickNext():
    global num
    num += 1
    if num > 8:
        num = 0
    label1.configure(text=fnameList[num])

def ClickPrev() :
        global num
        num -= 1
        if num < 0 :
            num = 8
        label1.configure(text=fnameList[num])
        

window.geometry("700x200")
window.title("사진 앨범 보기")

btnPrev = Button(window, text = "<< 이전", command = ClickPrev)
btnNext = Button(window, text = "다음 >>", command = ClickNext)

label1 = Label(window, text=fnameList[num], fg = "blue", font=("궁서체", 30))

btnPrev.place(x = 150, y = 10)
btnNext.place(x = 450, y = 10)
label1.place(x = 300, y = 10)

window.mainloop()
