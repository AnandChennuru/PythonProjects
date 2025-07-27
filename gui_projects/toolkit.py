from tkinter import *

window = Tk()

window.geometry("800x800")

calc_img = PhotoImage(file="images\\calculator64.png")
cont_img = PhotoImage(file="images\\contacts64.png")
bmi_img = PhotoImage(file="images\\bmi64.png")
watch_img = PhotoImage(file="images\\stopwatch64.png")
age_img = PhotoImage(file="images\\age64.png")

welcome = Button(window, text="✨ Welcome to the Simple Utility App ✨",
                font=("Garamond", 30))

calc = Button(window, text="Calculator",
              image=calc_img,
              bd=0,)
cont = Button(window, text="Contact Book",
              image=cont_img,
              bd=0)
bmi = Button(window, text="BMI Calculator",
             image=bmi_img,
             bd=0)
watch = Button(window, text="Stopwatch",
               image=watch_img,
               bd=0)
age = Button(window, text="Age Calculator",
             image=age_img,
             bd=0)


welcome.pack()
calc.pack(anchor=NW)
cont.pack(anchor=NW)
bmi.pack(anchor=NW)
watch.pack(anchor=NW)
age.pack(anchor=NW)



window.mainloop()



# menu = Label(window, text=("Choose an option from the menu below:\n" +
#                            "1. 🧮 Calculator\n" +
#                            "2. 📞 Contact Book\n" +
#                            "3. ⚖️ BMI Calculator\n" +
#                            "4. ⏱️ Stopwatch\n" +
#                            "5. 🎂 Age Calculator\n" +
#                            "6. 🚪 Exit\n"),
#              justify="left",
#              font=("Garamond", 15))
