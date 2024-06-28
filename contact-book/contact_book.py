from tkinter import *
root = Tk()

root.config(bg='#55AD9B')
root.title('phonebook')
root.geometry("550x450")

#set icon
root.wm_iconbitmap('ph.ico')

# function
def add_contact():
    name = txt.get()
    number =txt2.get()
#condition to check phone number is in proper digit before store.
    if number.isdigit() and len(number)==10:
        if name != "" and number !="":
            tasks.insert(END, 'name : ' +name+'   |  phone : '+number)
            txt.delete(0, END)
            txt2.delete(0,END)
        else:
            lbl_message.config(text="Please enter name")

    else:
        lbl_message.config(text="Pleas enter valid number.")

def delete_contact():
    try:
        selec_tas = tasks.curselection()[0]
        tasks.delete(selec_tas)
    except IndexError:
        lbl_message.config(text="Please select a contact to delete")

def delete_all():
    tasks.delete(0, END)

def update_contact():
    selected_task_index = tasks.curselection()
    if selected_task_index:
        name = txt.get()
        number = txt2.get()
        if name != "" and number != "":
            tasks.delete(selected_task_index[0])
            tasks.insert(selected_task_index[0], 'Name: ' + name + '   |  Phone: ' + number)
            txt.delete(0, END)
            txt2.delete(0, END)
        else:
            lbl_message.config(text="Please enter name", fg='red')
    else:
        lbl_message.config(text="Please select a contact to update", fg='red')

# Label
lbl = Label(root, text='phonebook', bg='#55AD9B',font='monospace 20 bold',fg='#26355D')
lbl.pack()

#warning label
lbl_message = Label(root, text="", bg='#55AD9B',fg='red',font='monospace 16 bold')
lbl_message.pack()




# Frame to hold
button_frame = Frame(root, bg='#55AD9B')
label1 = Label(root, text="Name :", font='monospace 20', background='#55AD9B')
label1.pack()
txt = Entry(root, width=50,font='monospace 20 ',background='#D8EFD3')
txt.pack()
label1 = Label(root, text="phone no :", font='monospace 20', background='#55AD9B')
label1.pack()
txt2 = Entry(root, width=50,font='monospace 20 ',background='#D8EFD3')
txt2.pack()
button_frame.pack()

# Add button
btn = Button(button_frame, text='Add contact', fg='#1679AB', bg='#97BE5A',font='monospace 12 bold', command=add_contact)
btn.pack(side=LEFT, padx=5)

# Delete button
btn_del = Button(button_frame, text='Delete', fg='#1679AB',font='monospace 12 bold', bg='#97BE5A', command=delete_contact)
btn_del.pack(side=LEFT, padx=5)

#update button
btn_upd = Button(button_frame, text='update contact', fg='#1679AB',font='monospace 12 bold', bg='#97BE5A', command=update_contact)
btn_upd.pack(side=LEFT, padx=5)


# Delete all button
btn_all = Button(button_frame, text='Delete All', fg='#1679AB',font='monospace 12 bold', bg='#97BE5A', command=delete_all)
btn_all.pack(side=LEFT, padx=5)

# Listbox
tasks = Listbox(root, width=45, height=15,font='verdana 12',background='#F1F8E8')
tasks.pack(pady=10)

# End loop
root.mainloop()
