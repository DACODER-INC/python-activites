from tkinter import *
from tkinter import messagebox
root = Tk()
root.title('Reading calculator if YOURE SOOOO LAZY YOU CANT DO IT YOURSELF')
root.geometry('500x300')

heading = Label(root, text='A schedule planner for reading cause your lazy bum wont do it yourself', font=("Arial", 18, 'bold'), bg='light blue')
heading.pack(pady=50)

instruction = Label(root, text='Click the button to calculate', bg='light blue')
instruction.pack(pady=10)

def topwin():
    top = Toplevel(root)
    top.title('Create the reading plan for your lazy bum')
    top.configure(bg='light grey')
    top.geometry('500x350+50+50')

    pages_label = Label(top, text='Enter total no. of pages lazy bum: ',bg='light grey' )
    pages_entry = Entry(top)

    daily_label = Label(top, text='Enter pages that u can do each day', bg='light grey')
    daily_entry = Entry(top)

    result_label = Label(top, text='Your reading plan (for now)', font=('Arial', 14, 'bold'), bg='light grey')

    days_label = Label(top, text='Complete these days', bg='light grey')

    remaining_label = Label(top, text='Pages left', bg='light grey')
    days_entry = Entry(top)
    remaining_entry = Entry(top)

    def calculate_plan():
        try:
            total_pages = int(pages_entry.get())
            pages_per_day = int(daily_entry.get())

            if total_pages <= 0 or pages_per_day <= 0:
                messagebox.showerror('Invalid Input', 'Please enter no.s greater than 0')
                return
            complete_days = total_pages // pages_per_day
            remaining_pages = total_pages % pages_per_day

            days_entry.delete(0, END)
            remaining_entry.delete(0, END)

            days_entry.insert(END, str(complete_days))
            remaining_entry.insert(END, str(remaining_pages))

        except ValueError:
            messagebox.showerror('Invald Input', 'Please enter valid whole no.s')
    calculate_button = Button(top, text='Create plan', command=calculate_plan, bg='#1261A0', fg='white')

    pages_label.place(x=80, y=40)
    pages_entry.place(x=280, y=40)

    daily_label.place(x=80, y=90)
    daily_entry.place(x=280, y=90)
    calculate_button.place(x=205, y=135)
    result_label.place(x=175, y=185)

    days_label.place(x=80, y=235)
    days_entry.place(x=280, y=235)
    remaining_label.place(x=80, y=275)
    remaining_entry.place(x=280, y=275)

start_button = Button(root, text='Create my reading plan', command=topwin, bg='#1261A0', fg='white')
start_button.pack(pady=15)
root.mainloop()