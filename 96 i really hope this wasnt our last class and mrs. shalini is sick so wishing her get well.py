from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
root = Tk()
root.title('My text editor')
root.geometry('600x500')
root.rowconfigure(0, minsize=800, weight=1)
root.columnconfigure(1, minsize=800, weight=1)

def open_file():
    filepath = askopenfilename(filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')])

    if not filepath:
        return


    txt_edit.delete(1.0, END)

    with open(filepath, 'r') as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)
        input_file.close()
        root.title(f'My text editor - {filepath}')

def save_file():
    filepath = asksaveasfilename(defaultextension='txt', filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')])
    
    if not filepath:
        return

    with open(filepath, 'w') as output_file:
        text = txt_edit.get(1.0, END)
        output_file.write(text)
        root.title(f'My text editor - {filepath}')

txt_edit = Text(root)
fr_bttns = Frame(root, relief = RAISED, bd=2)
bttn_open = Button(fr_bttns, text='Open', command=open_file)
bttn_save = Button(fr_bttns, text='Save As...', command=save_file)
bttn_open.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
bttn_save.grid(row=1, column=0, sticky='ew', padx=5)

fr_bttns.grid(row=0, column=0, sticky='ns')
txt_edit.grid(row=0, column=1, sticky='nsew')
root.mainloop()

