from tkinter import *

window = Tk()
window.geometry("500x600")
window.title("My first GUI")

icon = PhotoImage(file="images/logo.png")
window.iconphoto(True, icon)

window.mainloop()
