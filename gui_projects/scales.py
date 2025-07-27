from tkinter import *

def submit():
    print("Temp: " + str(scale.get()) + " deg. C")

window = Tk()

hotimg = PhotoImage(file="images\\hot64.png")
hotLabel = Label(window, image=hotimg)
hotLabel.pack()

scale = Scale(window, from_=100, to=0)
scale.config(fg="red", bg="#222222")
scale.config(activebackground="white")
scale.config(font=("garamond", 18))
scale.config(length=500)
# scale.config(orient=HORIZONTAL)
scale.config(tickinterval=10)
scale.config(showvalue=False)
scale.config(troughcolor="skyblue")

scale.set(50)

coldimg = PhotoImage(file="images\\cold64.png")
coldLabel = Label(window, image=coldimg)


bt = Button(window, text="Submit", command=submit)

scale.pack()
coldLabel.pack()
bt.pack()

window.mainloop()