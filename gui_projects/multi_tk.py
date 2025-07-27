from tkinter import *
from tkinter import colorchooser
import datetime
from tkinter.ttk import Combobox

# declare
wbcol, wfcol = "#d9d9d9", "#284b63"
current_date = datetime.datetime.now().strftime("%d %B %Y")
current_time = datetime.datetime.now().strftime("%I:%M %p")
frames = []
second = 0
minute = 0
hour = 0
t_id = None
currency_list = ["INR", "USD", "EUR", "JPY", "CAD"]
conversion_rates = {"INR": 1.0, "USD": 83.2, "EUR": 90.1, "JPY": 0.56, "CAD": 61.3}
selected_from = ""
selected_to = ""

def destroy_widgets():
    for widget in window.winfo_children():
        widget.destroy()
    frames.clear()
def calculator():
    destroy_widgets()
    window.geometry("")
    buttons = ['C', '0', '/','-','7', '8', '9','*','4', '5', '6', '+','1', '2', '3', '=']
    global ent_space
    eframe = Frame(window, border=5, bg=wfcol)
    eframe.pack()
    ent_space = Entry(eframe)
    ent_space.configure(width=16, bg=wbcol, fg=wfcol, font=("courier", 36), border=10, relief=SUNKEN)
    ent_space.pack(side=LEFT, fill=BOTH, padx=3)
    for i in range(4):
        frame = Frame(window, border=2, bg=wfcol)
        frame.pack()
        frames.append(frame)
    for i, val in enumerate(buttons):
        row = i // 4
        btn = Button(frames[row], text=val, width=7, height=2, font=("courier", 25), cursor="hand2")
        btn.configure(fg="white", bg=wfcol, activeforeground="white", activebackground=wfcol)
        btn.configure(command=lambda v=val: calc_operations(v))
        btn.pack(side="left")

    def backspace():
        ent_space.delete(len(ent_space.get())-1, END)

    bksp = Button(eframe, text="DEL", width=5, font=("courier", 25),fg="#EEF4ED", bg="#284b63", command=backspace,
                  activeforeground="#EEF4ED", activebackground="#284b63", cursor="hand2")
    bksp.pack(side=RIGHT, fill=BOTH, padx=3)
def calc_operations(x):
    if x == 'C':
        ent_space.delete(0, END)
    elif x == '=':
        try:
            result = eval(ent_space.get())
            ent_space.delete(0, END)
            ent_space.insert(0, str(result))
        except Exception:
            ent_space.delete(0, END)
            ent_space.insert(0, "Error")
    else:
        ent_space.insert(END, x)
def colorpicker():
    destroy_widgets()
    window.geometry("")
    color_code = colorchooser.askcolor(title="Choose a color", initialcolor="white")
    if color_code[1]:
        color_label = Label(window, font=("Segoe UI", 25, "bold"), text=color_code[1], bg=color_code[1], padx=10,
                            pady=10)
        color_label.place(relx=0.5, rely=0.5, anchor="center")
    else:
        window.destroy()
def stopwatch():
    destroy_widgets()
    window.geometry("")
    def start_time():
        global second, minute, hour
        h.config(text=f"{hour:02d}:")
        m.config(text=f"{minute:02d}:")
        s.config(text=f"{second:02d}")
        second += 1
        if second == 60:
            second = 0
            minute += 1
        if minute == 60:
            minute = 0
            hour += 1
        global t_id
        t_id = window.after(1000, start_time)
    def stop_time():
        global t_id
        if t_id is not None:
            window.after_cancel(t_id)
            t_id = None
    def use_time(t):
        if t == 1:
            start_time()
        elif t == 0:
            stop_time()
        else:
            global second, minute, hour
            stop_time()
            h.config(text="00:")
            m.config(text="00:")
            s.config(text="00")
            second = 0
            minute = 0
            hour = 0
    tframe = Frame(window, bg=wfcol, pady=30, padx=40)
    bframe = Frame(window, bg=wfcol, pady=40, padx=40)
    h = Label(tframe, text="00:", pady=20, font=("Courier", 20), bg=wfcol, fg="white")
    m = Label(tframe, text="00:", pady=20, font=("Courier", 20), bg=wfcol, fg="white")
    s = Label(tframe, text="00", pady=20, font=("Courier", 20), bg=wfcol, fg="white")
    start_watch = Button(bframe, text="Start", font=("Courier", 20, "bold"), bg=wbcol, fg=wfcol,
                         activeforeground=wfcol,activebackground=wbcol ,command=lambda: use_time(1), cursor="hand2")
    stop_watch = Button(bframe, text="Stop", font=("Courier", 20, "bold"), bg=wbcol, fg=wfcol,
                         activeforeground=wfcol,activebackground=wbcol ,command=lambda:
    use_time(0), cursor="hand2")
    reset_watch = Button(bframe, text="Reset", font=("Courier", 20, "bold"), bg=wbcol, fg=wfcol,
                         activeforeground=wfcol,activebackground=wbcol ,command=lambda:
    use_time(2), cursor="hand2")
    tframe.pack()
    bframe.pack(fill=BOTH)
    h.pack(side=LEFT)
    m.pack(side=LEFT)
    s.pack(side=LEFT)
    start_watch.pack(side=LEFT, fill=BOTH)
    stop_watch.pack(side=LEFT, fill=BOTH)
    reset_watch.pack(side=LEFT, fill=BOTH)
def converter():
    destroy_widgets()
    window.geometry("700x300")
    cust_font = ("Ariel", 20)
    window.option_add("*TCombobox*Listbox.font", cust_font)
    bframe = Frame(window, bg=wbcol)
    bdframe = Frame(bframe, bd=8, relief=RAISED, bg=wbcol)
    global selected_from, selected_to, ent_from, ent_to
    selected_from = StringVar()
    selected_to = StringVar()
    box_from = Combobox(bdframe, values=currency_list, textvariable=selected_from, state="readonly", font=cust_font)
    box_to = Combobox(bdframe, values=currency_list, textvariable=selected_to, state="readonly", font=cust_font)
    ent_from = Entry(bdframe, font=cust_font, fg=wbcol, bg=wfcol, border=5, insertbackground=wbcol)
    ent_to = Entry(bdframe, font=cust_font, fg=wbcol, bg=wfcol, border=5, insertbackground=wbcol)
    conv_btn = Button(bdframe, text="Convert", font=("Arial", 15, "bold"), fg=wfcol, command=convert_currency,
                      cursor="hand2")
    bframe.place(relx=0.5, rely=0.5, anchor=CENTER)
    bdframe.grid()
    ent_from.grid(row=0, column=0, pady=5, padx=5)
    box_from.grid(row=0, column=2, pady=15, padx=5)
    box_from.current(0)
    selected_from.set(currency_list[0])
    conv_btn.grid(row=2, column=0)
    ent_to.grid(row=3, column=0, pady=15, padx=5)
    box_to.grid(row=3, column=2, pady=5, padx=5)
    box_to.current(1)
    selected_to.set(currency_list[1])
def convert_currency():
    try:
        amount = float(ent_from.get())
        from_currency = selected_from.get()
        to_currency = selected_to.get()
        amount_in_inr = amount * conversion_rates[from_currency]
        converted_amount = amount_in_inr / conversion_rates[to_currency]
        ent_to.delete(0, END)
        ent_to.insert(0, f"{converted_amount:.2f}")
    except Exception as e:
        ent_to.delete(0, END)
        ent_to.insert(0, "Error")

window = Tk()
window.geometry("400x600+500+100")
window.config(bg="#284b63")
window.title("Multi Utility Tool-Kit")

logo = PhotoImage(file="images\\mutoolkit.png")
window.iconphoto(True, logo)

calc_icon = PhotoImage(file="images\\calc128.png")
cont_icon = PhotoImage(file="images\\color128.png")
stop_icon = PhotoImage(file="images\\stop128.png")
conv_icon = PhotoImage(file="images\\conv128.png")

h1 = Label(window, text=current_date+"\n"+current_time)
h1.configure(font=("Segoe UI", 20, "bold"),fg="white", bg="#284b63")
w1 = Button(window, text="Calculator", image=calc_icon, command=calculator, activebackground=wbcol, cursor="hand2")
w2 = Button(window, text="Colourpicker", image=cont_icon, command=colorpicker, activebackground=wbcol, cursor="hand2")
w3 = Button(window, text="Stopwatch", image=stop_icon, command=stopwatch, activebackground=wbcol, cursor="hand2")
w4 = Button(window, text="Converter", image=conv_icon, command=converter, activebackground=wbcol, cursor="hand2")
w1.configure(bg=wbcol, compound="top", padx=15, font=("Segoe UI", 16, "bold"), fg=wfcol, activeforeground=wfcol)
w2.configure(bg=wbcol, compound="top", padx=15, font=("Segoe UI", 16, "bold"), fg=wfcol, activeforeground=wfcol)
w3.configure(bg=wbcol, compound="top", padx=15, font=("Segoe UI", 16, "bold"), fg=wfcol, activeforeground=wfcol)
w4.configure(bg=wbcol, compound="top", padx=15, font=("Segoe UI", 16, "bold"), fg=wfcol, activeforeground=wfcol)
h1.place(x=200, y=65, anchor="center")
w1.place(x=105, y=220, anchor="center")
w2.place(x=295, y=220, anchor="center")
w3.place(x=105, y=420, anchor="center")
w4.place(x=295, y=420, anchor="center")

window.mainloop()