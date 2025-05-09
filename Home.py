from tkinter import *
import Scanner
import Add_user
from PIL import Image, ImageTk


window = Tk() #istantiate an instance of a window
window.geometry("1000x700") #width x height
window.title('Scanner')

window.config(background='black')
mainLabel = Label(window,
                  text = "Attendance Scanner", 
                  font = ('Arial',30,'bold'), 
                  fg = 'white', 
                  bg = 'black')
mainLabel.pack()

#Scan button
scanbtn = Button(window, width=8,height= 2, text = 'Scan')
scanbtn.config(command=Scanner.start_scanner)
scanbtn.config(font=('Arial', 20, 'bold'))
scanbtn.config(activebackground='red')

scanbtn.place(x=80, y=80)


#add user button
addusrbtn = Button(window, width=8,height=2,text = 'Add user')
addusrbtn.config(command=Add_user.add_window) #for function calling
addusrbtn.config(font=('Arial', 20, 'bold'))
addusrbtn.config(activebackground='red')

addusrbtn.place(x=250, y=80)


#delete user button
delusrbtn = Button(window, width=10, height = 2, text = 'Delete user')
delusrbtn.config()
delusrbtn.config(font=('Arial', 20, 'bold'))
delusrbtn.config(activebackground='red')

delusrbtn.place(x=420, y=80)


window.mainloop()