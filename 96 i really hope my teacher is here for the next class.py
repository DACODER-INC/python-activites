from tkinter import *
from tkinter import messagebox
root = Tk()
root.title('stupid annoying pop-up that will FREEZE EVERYTHING AND RUIN YOUR DAYYYYYYY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
root.geometry('200x200')

def msg():
    messagebox.showwarning('ALERT', 'STOP WHAT YOU ARE DOING THERE IS A VIRUS ON YOUR COMPUTER')

bttn = Button(root, text='SCAN YOUR COMPUTER', command=msg)
bttn.place(x=100, y=100)
root.mainloop()
