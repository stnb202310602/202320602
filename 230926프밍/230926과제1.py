from tkinter import *
window = Tk()

def myFunc():
    if chk.get() == 1:
        label2.configure(image=photo)
    elif chk.get() == 2:
        label2.configure(image=photo2)
    elif chk.get() == 3:
        label2.configure(image=photo3)


chk = IntVar()
label1 = Label(window, text = "좋아하는 동물 투표", font = ("궁서체", 30), fg = "blue")
photo = PhotoImage(file="/Users/kim_seong_kyeong/Library/CloudStorage/OneDrive-우송대학교(WOOSONGUNIVERSITY)/프로그래밍/jpeg/dog.gif")
photo2 = PhotoImage(file="/Users/kim_seong_kyeong/Library/CloudStorage/OneDrive-우송대학교(WOOSONGUNIVERSITY)/프로그래밍/jpeg/cat.gif")
photo3 = PhotoImage(file="/Users/kim_seong_kyeong/Library/CloudStorage/OneDrive-우송대학교(WOOSONGUNIVERSITY)/프로그래밍/jpeg/rabbit.gif")
label2 = Label(window, image=None)

button1 = Button(window, text="사진보기", command=myFunc)

rb1 = Radiobutton(window, text="dog", variable=chk, value=1)
rb2 = Radiobutton(window, text="cat", variable=chk, value=2)
rb3 = Radiobutton(window, text="rabbit", variable=chk, value=3)

label1.pack(); rb1.pack(); rb2.pack(); rb3.pack(); button1.pack(); label2.pack()

window.mainloop()