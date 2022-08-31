from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(str(letters[let])) for let in range(nr_letters)]
    password_list += [random.choice(str(symbols[sym])) for sym in range(nr_symbols)]
    password_list += [random.choice(str(numbers[num])) for num in range(nr_numbers)]

    # for char in range(nr_letters):
    #    password_list.append(random.choice(letters))

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    random.shuffle(password_list)
    password = "".join(password_list)
    # password = ""
   # for char in password_list:
    #    password += char
   # print(f"your password:{password}")
    pass_blank.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_blank.get()
    email = email_blank.get()
    password = pass_blank.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }

    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title=website, message=f"Enter mandatory fields to move forward")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_blank.delete(0, END)
            pass_blank.delete(0, END)
# ---------------------------Search Button ---------------------------- #

def find_password():
    website = website_blank.get()
    try:
        with open("data.json", "r") as data:
            data_file = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title="error", message="No data file found")
    else:
        if website in data_file:
            email = data_file[website]["email"]
            password = data_file[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \n Password: {password}")
        else:
            messagebox.showinfo(title=website, message=f"No data in file. Please add.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
pass_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_image)
canvas.grid(column=1, row=0)

website_label = Label(text="website:")
website_label.grid(column=0, row=1)
website_label.focus()
website_blank = Entry(width=17)
website_blank.grid(column=1, row=1)
website_search = Button(text="Search", width=15, command=find_password)
website_search.grid(column=2, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_blank = Entry(width=36)
email_blank.grid(column=1, row=2, columnspan=2)
email_blank.insert(0, "lathaec8@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
pass_blank = Entry(width=17)
pass_blank.grid(column=1, row=3)
pass_button = Button(text="Generate Password", command=password_generator)
pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()