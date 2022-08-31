from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


my_label = Label(text="I am a label", font=('arial',24, 'bold'))
my_label.grid(column=0, row=0)
my_label.config(text ="New Text")


def button_clicked():
    print("I got clicked")
    my_label.config(text ="Button Got Clicked")
    my_label.config(text=input.get())


button = Button(text= "click me", command=button_clicked)
button.grid(column=1, row=1)

button1 = Button(text= "new text",command=button_clicked)
button1.grid(column=2, row=0)

input = Entry(width=15)
input.grid(column=2, row=2)

my_label.config




window.mainloop()
