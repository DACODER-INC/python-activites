from tkinter import *
root = Tk()
root.title('Random thingy that shows an annoying pop-up every time i cick something just like an ad')
root.geometry('100x100')

def handle_keypress(event):
    print(event.char)
root.bind('<Key>', handle_keypress)

def handle_click(event):
    print('The button was clicked')

bttn = Button(text='Click me')
bttn.pack()

bttn.bind('<Button-1>', handle_click)
root.mainloop()