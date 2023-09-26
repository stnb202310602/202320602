from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("To-do List")

def add_Task():
    task = EntryTask.get() #텍스트 가져오기
    if task:
        TaskList.insert(END, task) #목록 끝에 task 추가
        EntryTask.delete(0, END)
    else:
        messagebox.showinfo("", "아무것도 입력되지 않음")

def del_Task():
    selectingTask = TaskList.curselection()
    if selectingTask:
        TaskList.delete(selectingTask)
    else:
        messagebox.showinfo("", "아무것도 선택되지 않음")

AddTask = Label(window, text="Add a Task:")
EntryTask = Entry(window, width = 30)
AddButton = Button(window, text="Add Task", command=add_Task)
DelButton = Button(window, text="delete", command=del_Task)
TaskList = Listbox(window, width=30)

AddTask.pack()
EntryTask.pack()
AddButton.pack()
TaskList.pack()
DelButton.pack()

window.mainloop()