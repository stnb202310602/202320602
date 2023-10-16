from tkinter import *
from tkinter import messagebox
import sqlite3

window = Tk()
window.title("GUI 데이터 입력")

con = sqlite3.connect("/Users/kim_seong_kyeong/Library/CloudStorage/OneDrive-우송대학교(WOOSONGUNIVERSITY)/프로그래밍/231010프밍/database/md202310602")
cur = con.cursor()
cur.execute("create table if not exists guiTable(id char(4), username char(15), email char(20), birthYear int)")

input_data = []

def add_Task():
    data1 = EntryTask1.get()
    data2 = EntryTask2.get()
    data3 = EntryTask3.get()
    data4 = EntryTask4.get()

    if data1 and data2 and data3 and data4:
        #이메일을 기준으로 중복체크
        cur.execute("SELECT * FROM guiTable WHERE email=?", (data3,))
        existing_data = cur.fetchone()

        if existing_data:
            messagebox.showinfo("", "이미 존재하는 데이터입니다.")
        else:
            cur.execute("INSERT INTO guiTable VALUES (?, ?, ?, ?)", (data1, data2, data3, int(data4)))

            con.commit()

            EntryTask1.delete(0, END)
            EntryTask2.delete(0, END)
            EntryTask3.delete(0, END)
            EntryTask4.delete(0, END)

            messagebox.showinfo("", "데이터 입력 성공")
        
    else:
        messagebox.showinfo("", "모든 엔트리에 값을 입력하세요.")

def view_data():
    TaskList1.delete(0, END)
    TaskList2.delete(0, END)
    TaskList3.delete(0, END)
    TaskList4.delete(0, END)

    cur.execute("SELECT * FROM guiTable")
    rows = cur.fetchall()

    if rows:
        header = [description[0] for description in cur.description]

        TaskList1.insert(END, "----------------")
        TaskList2.insert(END, "----------------")
        TaskList3.insert(END, "----------------")
        TaskList4.insert(END, "----------------")

        for row in rows:
            TaskList1.insert(END, row[0])
            TaskList2.insert(END, row[1])
            TaskList3.insert(END, row[2])
            TaskList4.insert(END, row[3])

        # 헤더 출력
        TaskList1.insert(0, header[0])
        TaskList2.insert(0, header[1])
        TaskList3.insert(0, header[2])
        TaskList4.insert(0, header[3])
    else:
        messagebox.showinfo("", "데이터가 존재하지 않습니다")


EntryTask1 = Entry(window, width=7)
EntryTask2 = Entry(window, width=7)
EntryTask3 = Entry(window, width=7)
EntryTask4 = Entry(window, width=7)

EntryTask1.place(x=60, y=30)
EntryTask2.place(x=160, y=30)
EntryTask3.place(x=260, y=30)
EntryTask4.place(x=360, y=30)

AddButton = Button(window, text="Add Task", command=add_Task)
AddButton.place(x=460, y=30)

ViewButton = Button(window, text="View", command=view_data)
ViewButton.place(x=560, y=30)

TaskList1 = Listbox(window, width=15, height=15)
TaskList2 = Listbox(window, width=15, height=15)
TaskList3 = Listbox(window, width=15, height=15)
TaskList4 = Listbox(window, width=15, height=15)

TaskList1.place(x=10, y=70)
TaskList2.place(x=180, y=70)
TaskList3.place(x=350, y=70)
TaskList4.place(x=520, y=70)

def on_closing():
    con.commit()
    con.close()
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)

window.geometry("720x400")  # 가로 x 세로

window.mainloop()
