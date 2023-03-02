from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)

    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website_name = website_entry.get()
    email_name = email_entry.get()
    password = pass_entry.get()
    new_data = {
        website_name: {
            "email": email_name,
            "password": password,

        }
    }
    if len(pass_entry.get()) == 0 or len(website_entry.get()) == 0:
        messagebox.showinfo(title="Empty Fields", message="You have not filled out all fields")
    else:
        try:
            with open("passwords.json", "r") as f:
                # reading old data
                data = json.load(f)
        except FileNotFoundError:
            with open("passwords.json", "w") as f:
                # reading old data
                json.dump(new_data, f, indent=4)
        else:

            # Updating old data
            data.update(new_data)

            with open("passwords.json", "w") as f:

                # Saving updated data
                json.dump(data, f, indent=4)

        finally:
            website_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website_name = website_entry.get()
    try:
        with open("passwords.json") as data_file:
            data = json.load(data_file)
            checkpass = data[f'{website_name}']['password']
            checkemail = data[f'{website_name}']['email']
            messagebox.showinfo(title=f"{website_name}", message=f"The email for this website is {checkemail} \nThe password for this website is : {checkpass}")
    except KeyError:
        messagebox.showinfo(title="Error", message=f"No details for {website_name}")











# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20)

canvas = Canvas(width=200, height=200)

pass_img = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=pass_img)
canvas.grid(row=0, column=1)

website = Label(text="Website:")
website.grid(row=1, column=0)

email = Label(text="Email/Username:")
email.grid(row=2, column=0)

password = Label(text="Password:")
password.grid(row=3, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35, )
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "user123@gmail.com")

pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1)

search = Button(text="Search", width = 13, command=search_password)
search.grid(column=2, row=1, columnspan=2)

gen_pass = Button(text="Generate Password", command=generate_password)
gen_pass.grid(row=3, column=2)

add = Button(text="Add", width=36, command=add)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
