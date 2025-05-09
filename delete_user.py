from tkinter import *
from tkinter import ttk
import tkinter


def add_window():
    adduserwindow = Toplevel()
    adduserwindow.geometry("1000x700")
    adduserwindow.title("Scanner - ADD USER")
    adduserwindow.config(bg='#113136')


    dept_list = ['Computer Science & Engineering',
                 'Civil Engineering',
                 'Electrical & Electronics Engineering',
                 'Electrical & Communication Engineering']

    # Centered title
    mainAddLabel = Label(adduserwindow,
                         text="Attendance Scanner",
                         font=('Arial', 30, 'bold'),
                         fg='white',
                         bg='black')
    mainAddLabel.pack(pady=20)

    # Left-aligned frame for form inputs
    form_frame = Frame(adduserwindow, bg='#113136',relief='sunken', bd=50)
    form_frame.place(x=50,y=100) # Left side and fill vertically

    # Right-aligned frame for profile picture
    profile_frame = Frame(adduserwindow, highlightbackground="white", relief='sunken')
    profile_frame.place(x=150,y=100,height=105)

    label_font = ('Arial', 15, 'bold')
    label_bg = '#113136'
    label_fg = 'white'
    label_width = 20

    # Name
    name_label = tkinter.Label(form_frame, text='Enter Name', font=label_font,
                               bg=label_bg, fg=label_fg, width=label_width, anchor='w')
    name_label.grid(row=0, column=0, padx=10, pady=10)
    name_textbox = tkinter.Entry(form_frame, width=40)
    name_textbox.grid(row=0, column=1, padx=10, pady=10)

    # Roll Number
    roll_label = tkinter.Label(form_frame, text='Enter Roll Number', font=label_font,
                               bg=label_bg, fg=label_fg, width=label_width, anchor='w')
    roll_label.grid(row=1, column=0, padx=10, pady=10)
    roll_textbox = tkinter.Entry(form_frame, width=40)
    roll_textbox.grid(row=1, column=1, padx=10, pady=10)

    # Department
    dept_label = tkinter.Label(form_frame, text='Enter Department', font=label_font,
                               bg=label_bg, fg=label_fg, width=label_width, anchor='w')
    dept_label.grid(row=2, column=0, padx=10, pady=10)
    dept_combobox = ttk.Combobox(form_frame,value=dept_list,width=37)
    dept_combobox.grid(row = 2,column = 1,padx=10,pady=10)


    adduserwindow.mainloop()