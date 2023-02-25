from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
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

    if len(email_entry.get()) == 0 or len(pass_entry.get()) == 0 or len(website_entry.get()) == 0:
        messagebox.showinfo(title="Empty Fields", message="You have not filled out all fields")
    else:
        is_ok = messagebox.askokcancel(title=website_name,
                                       message=f"These are the details entered: \nEmail: {email_name}"
                                               f"\nPassword: {password} \nIs it ok to save?")



    if is_ok == TRUE:
        messagebox.showinfo(title="Alert!!", message="Password Added to List")

        with open("passwords.txt", "a") as f:
            f.write(f"{website_name} | {email_name} | {password}\n")
            website_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)

pass_img = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=pass_img)
canvas.grid(column=1, row=0)

website = Label(text="Website:", highlightthickness=0)
website.grid(column=0, row=1)

email = Label(text="Email/Username:", highlightthickness=0)
email.grid(column=0, row=2)

password = Label(text="Password:", highlightthickness=0)
password.grid(column=0, row=3)

website_entry = Entry(width=35, highlightthickness=0)
website_entry.grid(column=1, row=1, columnspan=2)

email_entry = Entry(width=35, highlightthickness=0)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "shanebarden10@gmail.com")

pass_entry = Entry(width=21, highlightthickness=0)
pass_entry.grid(column=1, row=3)

gen_pass = Button(text="Generate Password", highlightthickness=0, command=generate_password)
gen_pass.grid(column=2, row=3)

add = Button(text="Add", width=36, highlightthickness=0, command=add)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()
