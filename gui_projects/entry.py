from tkinter import *

window = Tk()

def submit():
    name = entry.get()
    print("Hello " + name)

def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get())-1, END)

entry = Entry()
entry.config(font=("garamond", 30))
entry.config(bg="#4d1402")
entry.config(fg="#42f5f2")

# entry.config(width=10)
# entry.config(show="*") for password
# entry.insert(0, "text here") sample text
# entry.config(state=DISABLED) ACTIVE/DISABLED

submit = Button(window, text="Submit", command=submit)
delete = Button(window, text="Delete", command=delete)
backspace = Button(window, text="Backspace", command=backspace)

entry.pack(side=LEFT)
submit.pack(side=RIGHT)
delete.pack(side=RIGHT)
backspace.pack(side=RIGHT)

window.mainloop()