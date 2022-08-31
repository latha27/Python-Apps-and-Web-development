from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=300)
window.config(padx=20, pady=20)


def calculate():
    miles = float(miles_input.get())
    result_label = round((1.609 * miles),2)
    kilometer_result_label.config(text=f"{result_label}")


miles_input = Entry()
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=3)



window.mainloop()
