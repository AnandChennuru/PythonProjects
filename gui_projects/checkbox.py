from tkinter import *

def disp():
    if (x.get()==1) & (y.get()==0):
        print("I play Football!")
    elif (x.get()==0) & (y.get()==1):
        print("I play Basketball!")
    elif (x.get()==1) & (y.get()==1):
        print("I play both Football and Basketball!")
    else:
        print("I don't play either")


window = Tk()

x = IntVar()
y = IntVar()

ft_img = PhotoImage(file="images\\football64.png")
bk_img = PhotoImage(file="images\\basketball64.png")

checkbox = Checkbutton(window, text='Football', variable=x, onvalue=1, offvalue=0, command=disp)
checkbox.config(font=("garamond", 20, 'bold'))
checkbox.config(fg='yellow')
checkbox.config(bg='brown')
checkbox.config(activeforeground='yellow')
checkbox.config(activebackground='brown')
checkbox.config(image=ft_img, compound=LEFT)
checkbox.config(padx=12, pady=20, width=200, height=30)
checkbox.config(selectcolor='darkgrey')

checkbox1 = Checkbutton(window, text='Basketball', variable=y, onvalue=1, offvalue=0, command=disp)
checkbox1.config(font=("garamond", 20, 'bold'))
checkbox1.config(fg='yellow')
checkbox1.config(bg='brown')
checkbox1.config(activeforeground='yellow')
checkbox1.config(activebackground='brown')
checkbox1.config(image=bk_img, compound=LEFT)
checkbox1.config(padx=12, pady=20, width=200, height=30)
checkbox1.config(selectcolor='darkgrey')


checkbox.pack(anchor='w')
checkbox1.pack(anchor='w')

window.mainloop()