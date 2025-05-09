from tkinter import *
from tkinter import ttk, filedialog
from PIL import ImageTk, Image


def add_window():
    adduserwindow = Toplevel()
    adduserwindow.geometry("1000x700")
    adduserwindow.title("Scanner - ADD USER")
    adduserwindow.config(bg='#113136')

    dept_list = ['Computer Science & Engineering',
                 'Civil Engineering',
                 'Electrical & Electronics Engineering',
                 'Electrical & Communication Engineering']

    # === Profile Image Reference ===
    adduserwindow.profile_image = None

    # === Function to Browse and Display Image ===
    def selectPic():
        filename = filedialog.askopenfilename(
            parent=adduserwindow,
            title="Select Image",
            filetypes=(("PNG files", "*.png"), ("JPG files", "*.jpg"), ("All files", "*.*"))
        )
        if filename:
            img = Image.open(filename)
            img = img.resize((150, 150), Image.Resampling.LANCZOS)
            img = ImageTk.PhotoImage(img)

            # Keep reference
            adduserwindow.profile_image = img
            profile_label.configure(image=img)

    # === Title ===
    mainAddLabel = Label(adduserwindow,
                         text="Attendance Scanner",
                         font=('Arial', 30, 'bold'),
                         fg='white',
                         bg='black')
    mainAddLabel.pack(pady=20)

    # === Left Frame ===
    form_frame = Frame(adduserwindow, bg='#113136', relief='sunken', bd=5)
    form_frame.place(x=50, y=100)

    # === Right Frame for Image ===
    profile_frame = Frame(adduserwindow, bg='white', width=150, height=150)
    profile_frame.place(x=800, y=100)
    profile_frame.pack_propagate(False)  # Prevent resizing

    # Label to hold image
    profile_label = Label(profile_frame, bg='white')
    profile_label.pack(expand=True, fill='both')

    # Browse Button
    pic_browsebtn = Button(adduserwindow, text='Select Image', command=selectPic)
    pic_browsebtn.place(x=825, y=270)

    # === Fonts and Colors ===
    label_font = ('Arial', 15, 'bold')
    label_bg = '#113136'
    label_fg = 'white'
    label_width = 20

    # === Form Inputs ===
    # Name
    name_label = Label(form_frame, text='Enter Name', font=label_font,
                       bg=label_bg, fg=label_fg, width=label_width, anchor='w')
    name_label.grid(row=0, column=0, padx=10, pady=10)
    name_textbox = Entry(form_frame, width=40)
    name_textbox.grid(row=0, column=1, padx=10, pady=10)

    # Roll Number
    roll_label = Label(form_frame, text='Enter Roll Number', font=label_font,
                       bg=label_bg, fg=label_fg, width=label_width, anchor='w')
    roll_label.grid(row=1, column=0, padx=10, pady=10)
    roll_textbox = Entry(form_frame, width=40)
    roll_textbox.grid(row=1, column=1, padx=10, pady=10)

    # Department
    dept_label = Label(form_frame, text='Enter Department', font=label_font,
                       bg=label_bg, fg=label_fg, width=label_width, anchor='w')
    dept_label.grid(row=2, column=0, padx=10, pady=10)
    dept_combobox = ttk.Combobox(form_frame, value=dept_list, width=37)
    dept_combobox.grid(row=2, column=1, padx=10, pady=10)

    adduserwindow.mainloop()
