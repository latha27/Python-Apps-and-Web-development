from tkinter import *
import requests


def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    response_quote = response.json()["quote"]
    canvas.itemconfig(created_text, text=response_quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=300, height=414, bg="white")
back_image = PhotoImage(file="background.png")
created_canvas_image = canvas.create_image(150, 207, image=back_image)
created_text = canvas.create_text(150, 200, text="Kanye Quote",width=250, font=("Arial", 15, "italic"))
canvas.grid(row=8, column=8)

kanya_image = PhotoImage(file="kanye.png")
kanya_button = Button(image=kanya_image, highlightthickness='0', command=get_quote)
kanya_button.grid(row=9, column=8)


get_quote()

window.mainloop()
