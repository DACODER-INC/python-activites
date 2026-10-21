from tkinter import*

root = Tk()
root.title('Create an account so we can collect you data and give it to SI not ai because trump changed it')
root.geometry('400x400')
frame = Frame(master=root, height=200, width=360, bg='#d0efff')

lbl1 = Label(frame, text='Full Name', bg='#3895d3', fg='white', width=12)
lbl2 = Label(frame, text='Email', bg='#3895d3', fg='white', width=12)
lbl3 = Label(frame, text='Password', bg='#3895d3', fg='white', width=12)

name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame, show = '*')

def display():
    name = name_entry.get()
    greet = 'Hey ' + name
    message = '\n Thanks for making an account so we can feed it to SI'
    text_box.insert(END, greet)
    text_box.insert(END, message)


text_box = Text(bg = '#BEBEBE', fg='black')
button = Button(text='Create account', command=display, bg='red')

frame.place(x=20,y=0)

lbl1.place(x=20, y=20)

name_entry.place(x=150, y=20)

lbl2.place(x=20, y=80)

email_entry.place(x=150, y=80)

lbl3.place(x=20, y=140)

pass_entry.place(x=150, y=140)

button.place(x=130, y=210)

text_box.place(y=250)
root.mainloop()