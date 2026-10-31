from tkinter import *
root = Tk()
root.title('IF you thought that popup that we did earlier was annoying just wait till you see this one')
root.geometry('700x700')


def topwin():
    top = Toplevel()
    top.title('This is the annoying popup i was talking about in the root window right beside this window')
    top.geometry('500x500')
    lb = Label(top, text='HAHAHAHHAHHAHAHAHAHAHAHA GET HACKED IDIOT')
    lb.pack()
    

bttn = Button(root, text='Click here for free bobux', bg='grey', fg='black', command=topwin)
bttn.place(x=250, y=350)
root.mainloop()