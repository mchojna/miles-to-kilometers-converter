import tkinter


def change():
    global text_1
    global text_2
    global to_kilometers

    text_1.destroy()
    text_2.destroy()

    if to_kilometers:
        text_1_text = "Kilometers"
        text_2_text = "Miles"
        to_kilometers = False
    else:
        text_1_text = "Miles"
        text_2_text = "Kilometers"
        to_kilometers = True

    text_1 = tkinter.Label(text=f"{text_1_text}:", font=("Arial", 20, "bold"))
    text_1.place(x=15, y=65)

    text_2 = tkinter.Label(text=f"{text_2_text}:", font=("Arial", 20, "bold"))
    text_2.place(x=15, y=125)


def convert():
    global to_kilometers

    entry_2.delete(0, 'end')
    round_value = int(spinbox.get())
    entry_1_variable = float(entry_1.get())

    if to_kilometers:
        variable = entry_1_variable / 0.6213712
        converted_variable = (round(variable, round_value))
    else:
        variable = entry_1_variable * 0.6213712
        converted_variable = (round(variable, round_value))

    entry_2.insert(0, str(converted_variable))


to_kilometers = True

window = tkinter.Tk()
window.title("Converter")
window.minsize(width=230, height=300)

title = tkinter.Label(text="Converter", font=("Arial", 30, "bold"))
title.place(x=40, y=15)

text_1 = tkinter.Label(text="Miles:", font=("Arial", 20, "bold"))
text_1.place(x=15, y=65)

text_2 = tkinter.Label(text="Kilometers:", font=("Arial", 20, "bold"))
text_2.place(x=15, y=125)

text_3 = tkinter.Label(text="Round:", font=("Arial", 20, "bold"))
text_3.place(x=15, y=185)

spinbox = tkinter.Spinbox(from_=0, to=5, width=1)
spinbox.place(x=90, y=187)

button_1 = tkinter.Button(text="Change", font=("Arial", 14, "bold"), command=change)
button_1.place(x=70, y=225)

# button to change
button_2 = tkinter.Button(text="Convert", font=("Arial", 14, "bold"), command=convert)
button_2.place(x=70, y=260)

# entry 1
entry_1 = tkinter.Entry()
entry_1.focus()
entry_1.place(x=15, y=95)

# entry 2
entry_2 = tkinter.Entry()
entry_2.place(x=15, y=155)


window.mainloop()
