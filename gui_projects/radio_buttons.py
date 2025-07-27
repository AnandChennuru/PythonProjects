from tkinter import *

games = ["Football", "Basketball", "Badminton"]

def select():
    if x.get() == 0:
        print("I play Football")
    elif x.get() == 1:
        print("I play Basketball")
    elif x.get() == 2:
        print("I play Badminton")
    else:
        print("What?")

window = Tk()

window.configure(bg='black')

ft_img = PhotoImage(file="images\\football64.png")
bk_img = PhotoImage(file="images\\basketball64.png")
bd_img = PhotoImage(file="images\\shuttlecock64.png")
games_imgs = [ft_img, bk_img, bd_img]

x = IntVar()


for i in range(len(games)):
    radio = Radiobutton(window, text=games[i], variable=x, value=i)
    radio.config(font=('garamond', 25))
    radio.config(fg='yellow')
    radio.config(bg='brown')
    radio.config(activeforeground='yellow')
    radio.config(activebackground='brown')
    radio.config(image=games_imgs[i])
    radio.config(compound="left")
    radio.config(padx=20, pady=10)
    radio.config(width=300)
    radio.config(selectcolor="skyblue")
    radio.config(indicatoron=False)
    radio.config(command=select)

    radio.pack(anchor=W)
window.mainloop()