from tkinter import *

root = Tk()

#colors
bg_color = '#006769'
fg_color = '#40A578'
acc_color = '#9DDE8B'
highlight = '#E6FF94'

root.config(bg=bg_color)
root.title('ToDooo')
root.geometry("600x400")

#icon
root.wm_iconbitmap('todo.ico')

# Create function for buttons
def add_task():
    task = txt.get()
    if task != "":
        tasks.insert(END, task)
        txt.delete(0, END)
    else:
        lbl_dis.config(text="Please enter a task", fg='red')

def delete_task():
    selected_task_index = tasks.curselection()
    if selected_task_index:
        tasks.delete(selected_task_index[0])
    else:
        lbl_dis.config(text="Please select a task to delete", fg='red')

def delete_all():
    tasks.delete(0, END)

def update_task():
    selected_task = tasks.curselection()
    if selected_task:
        selected_task = selected_task[0]
        new_task_text = txt.get()
        if new_task_text != "":
            tasks.delete(selected_task)
            tasks.insert(selected_task, new_task_text)
            txt.delete(0, END)
        else:
            lbl_dis.config(text="Please enter a task", fg='red')
    else:
        lbl_dis.config(text="Please select a task to update", fg='red')

# Label
lbl = Label(root, text='To-Do List', bg=bg_color, font='Arial 20 bold', fg=highlight)
lbl.pack(pady=10)

# Warning label
lbl_dis = Label(root, text="", bg=bg_color, fg='red', font='Arial 12 bold')
lbl_dis.pack()

# Textbox with small font
txt = Entry(root, width=50, font='Arial 14')
txt.pack(pady=10)

# Frame
button_frame = Frame(root, bg=bg_color)
button_frame.pack()

# Add button
btn_add = Button(button_frame, text='Add Task', fg=fg_color, bg=acc_color, font='Arial 12 bold', command=add_task)
btn_add.pack(side=LEFT, padx=5)

# Delete button
btn_del = Button(button_frame, text='Delete Task', fg=fg_color, font='Arial 12 bold', bg=acc_color, command=delete_task)
btn_del.pack(side=LEFT, padx=5)

# Update button
btn_update = Button(button_frame, text='Update Task', fg=fg_color, font='Arial 12 bold', bg=acc_color, command=update_task)
btn_update.pack(side=LEFT, padx=5)

# Delete all button
btn_all = Button(button_frame, text='Delete All', fg=fg_color, font='Arial 12 bold', bg=acc_color, command=delete_all)
btn_all.pack(side=LEFT, padx=5)

# Listbox with large font
tasks = Listbox(root, width=45, height=15, font='Arial 16', bg=highlight, selectbackground=acc_color, selectforeground=fg_color)
tasks.pack(pady=10)

root.mainloop()
