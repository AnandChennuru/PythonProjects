from tkinter import *

c = 0

def sum():
    c = int(a_entry.get()) + int(b_entry.get())
    c_disp.config(text=c)


window = Tk()

a_entry = Entry(window)
a_entry.config(width=20)
a_entry.config(font=("consolas", 20))
a_entry.config(fg='yellow', bg='brown')

b_entry = Entry(window)
b_entry.config(width=20)
b_entry.config(font=("consolas", 20))
b_entry.config(fg='yellow', bg='brown')

c_disp = Label(window, text=c)
c_disp.config(font=("garamond", 25))
c_disp.config(fg='brown')

add = Button(window, text="Add")
add.config(command=sum)

a_entry.pack()
b_entry.pack()
c_disp.pack()
add.pack()

window.mainloop()