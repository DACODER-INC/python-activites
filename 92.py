from tkinter import *
from datetime import date
window = Tk()
window.title('random name and date form')
window.geometry('400x300')
lbl = Label(text = 'hey there', fg = 'white', bg = '#072F5F', height = 1, width = 300)
name_lbl = Label(text = 'Full name', bg = '#3895D3')
name_entry = Entry()
def display():
    name = name_entry.get()
    global message
    message = 'Welcome to the application that i just created for you! \n Here is todays date '
    greet = 'Hello ' + name + '\n'
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box = Text(height = 3)
btn = Button(text = 'begin', command = display, height = 1, bg = '#1261A0', fg = 'white')
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
window.mainloop()