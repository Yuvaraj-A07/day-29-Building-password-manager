import json
from tkinter import *
from tkinter import messagebox as mb
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project

def password_manager():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    lett = [password_list.append(random.choice(letters)) for char in range(nr_letters)]

    sym = [password_list.append(random.choice(symbols)) for char in range(nr_symbols)]

    num = [password_list.append(random.choice(numbers)) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    # print(f"Your password is: {password}")
    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def find_password():
    web = web_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        mb.showinfo(title="Error", message="No Data file found")
    else:

        try:
            email = data[web]["email"]
            password = data[web]["password"]
        except KeyError:
            mb.showinfo(title=web, message=f"No details for the website exits")
        else:
            mb.showinfo(title=web, message=f"email: {email}\npassword: {password}")


def save():
    web = web_entry.get()
    e_mail = email_entry.get()
    passwords = pass_entry.get()
    new_data = {
        web: {
            "email": e_mail,
            "password": passwords
        }
    }
    if len(web) == 0 or len(passwords) == 0:
        mb.showinfo(title="Opps", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading the old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating the old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #saving the updated file
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, "end")
            pass_entry.delete(0, "end")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

#entry

web_entry = Entry(width=21)
web_entry.grid(column=1, row=1)
web_entry.focus()
#website label
label = Label(text="Website:", font=("Arial", 12, "normal"))
label.grid(column=0, row=1)

#email

email_entry = Entry(width=45)
email_entry.insert(0, "yuvaraj@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

#email label
e_label = Label(text="Email/Username:", font=("Arial", 12, "normal"))
e_label.grid(column=0, row=2)

#password

pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3)

#pass label
pass_label = Label(text="Password:", font=("Arial", 12, "normal"))
pass_label.grid(column=0, row=3)

#generate pass button

pass_button = Button(text="Generate password", command=password_manager)
pass_button.grid(column=2, row=3)

# Add button

add = Button(text="Add", width=36, command=save)
add.grid(column=1, row=4, columnspan=2)

# search Button
search = Button(text="Search", width=15, command=find_password)
search.grid(column=2, row=1)








window.mainloop()