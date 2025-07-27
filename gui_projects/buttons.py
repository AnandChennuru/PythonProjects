from tkinter import *

count = 0

def press():
    # print("Hello!")
    global count
    count += 1
    count_label.config(text=count)
    if count==2:
        warn.pack()
    elif count==5:
        warn1.pack()
    elif count==10:
        button.config(state=DISABLED)
        warn2.pack()


window = Tk()

window.geometry("400x400")

pic = PhotoImage(file="images\\point64.png")
img = PhotoImage(file="images\\point64.png")

# button is clickable
button = Button(window, text="Don't Click!!!")

# .config used for further EDITING of our widgets
button.config(command=press)  # here press is fn name used as call back
button.config(font=("courier", 20, "bold"))
button.config(bg="#98dffc")
button.config(fg="black")
button.config(activebackground="#76bdda")
button.config(activeforeground="black")
button.config(image=pic)
button.config(compound="bottom")

count_label = Label(window, text=count,
                    font=("Times", 20, "bold"))

warn = Label(window, text="Ahh! I said NO!",
             font=('garamond', 12))
warn1 = Label(window, text="I'm warning you now!!!",
              font=('garamond', 12))
warn2 = Label(window, text="Control Overflowed!!! Severe Damage to the button!",
              fg="red",
              font=('garamond', 12))


img_label = Label(window, image=img)

count_label.pack()
button.pack()

window.mainloop()