from tkinter import *
from tkinter.ttk import Combobox

window = Tk()
window.geometry("500x200")

currency_list = ["Indian Rupee (INR)", "US dollar (USD)", "Euro (EUR)", "Japanese yen (JPY)", "Canadian dollar (CAD)"]

selected_from = StringVar()

box = Combobox(window, values=currency_list, textvariable=selected_from, state="readonly", font=("Arial", 20))
box.grid(row=0, column=0, padx=20, pady=20)

box.current(0)
selected_from.set(currency_list[0])

print("Selected:", selected_from.get())

window.mainloop()
