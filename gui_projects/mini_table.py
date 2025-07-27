from tkinter import *
from tkinter.ttk import Combobox

currency_list = ["Indian Rupee (INR)", "US dollar (USD)", "Euro (EUR)", "Japanese yen (JPY)", "Canadian dollar (CAD)"]

window = Tk()
window.geometry("700x300")
window.configure(bg="#1B263B")

cust_font = ("Ariel", 20)
window.option_add("*TCombobox*Listbox.font", cust_font)

bframe = Frame(window, bg="#1B263B")
bdframe = Frame(bframe, bd=5, relief=RAISED, bg="#1B263B")

selected_from = StringVar()
selected_to = StringVar()

box_from = Combobox(bdframe, values=currency_list, textvariable=selected_from, state="readonly", font=cust_font)
box_from.current(0)
box_to = Combobox(bdframe, values=currency_list, textvariable=selected_to, state="readonly", font=cust_font)
box_to.current(1)
ent_from = Entry(bdframe, font=cust_font)
ent_to = Entry(bdframe, font=cust_font)
conv_btn = Button(bdframe, text="Convert", font=("Arial", 15))



bframe.place(relx=0.5, rely=0.5, anchor=CENTER)
bdframe.grid()
ent_from.grid(row=0, column=0, pady=5, padx=5)
box_from.grid(row=0, column=2, pady=15, padx=5)
conv_btn.grid(row=2, column=0)
ent_to.grid(row=3, column=0, pady=15, padx=5)
box_to.grid(row=3, column=2, pady=5, padx=5)

window.mainloop()