from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Some after school routine checker of somesort that idk what will do')
root.geometry('400x320')

heading = Label(root, text='my after school routine checker or list of some sort', font = ('Arial', 16, 'bold'))
heading.pack(pady=10)
instruction = Label(root, text='Enter your next after school task')
instruction.pack()

task_entry = Entry(root, width=35)
task_entry.pack(pady=8)

key_label = Label(root, text='Last key preesed: None')
key_label.pack(pady=5)

def handle_keypress(event):
    key_label.config(text='Last key preesed: ' + event.char)

task_entry.bind('<Key>', handle_keypress)

def handle_click(event):
    routine_message.config(text='Routine area clicked')

routine_message = Label(root, text='Click here to view your routine', bg='#d0efff', width=32, height=3)
routine_message.pack(pady=10)

routine_message.bind('<Button-1>', handle_click)

def check_routine():
    task = task_entry.get()

    if task == '':
        messagebox.showwarning('Missing Task', 'Please enter a task so we can add it')
    else:
        routine_message.config(text='Next task: ' + task)

check_button = Button(root, text='Check my routine', command=check_routine)
check_button.pack(pady=10)

root.mainloop()