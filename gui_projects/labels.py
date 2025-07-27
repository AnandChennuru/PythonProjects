from tkinter import *

window = Tk()

window.geometry("800x600")

photo = PhotoImage(file="images\\earth32.png")
pic2 = PhotoImage(file="images\\settings32.png")
pic3 = PhotoImage(file="images\\browser32.png")

# window.geometry("400x400")

# label = Label(window, text="Hello, World!") Simple label

label = Label(window, text="Hello, World!",
              font=("garamond", 30),
              fg="yellow",
              bg="brown",
              relief='raised',
              bd="7",
              padx=20,
              pady=10,
              image=photo,
              compound='left')

label1 = Label(window, text="This is me creating widgets for the first time!",
               font=("Garamond", 15))

left = Label(window, text="Hello there...",
             font=("Garamond", 12),
             image=pic2,
             compound='bottom')

right = Label(window, text="Look here...",
              font=("Garamond", 12),
              image=pic3,
              compound='bottom')

# label.pack() fixed position
label.pack()
label1.pack()

# label.place(x=40,y=50) customisation of axes
left.place(x=40, y=300)
right.place(x=680, y=300)


window.mainloop()
