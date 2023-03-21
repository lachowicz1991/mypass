import random
import pyperclip
import tkinter as tk
import validators
import json
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, tk.END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    web = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        web: {"email":email, "password":password}
    }
    if not validators.url(f'http://{web}') and not validators.url(web):
        messagebox.showinfo(title="Lol?", message="Incorrect url.")
    elif len(password) < 6:
        messagebox.showinfo(title="Wtf", message="Shit password, less than 6 characters, try harder.")
    else:
        # is_correct = messagebox.askokcancel(title='Confirm',
        #                                     message=f'Website:{web}\nEmail:{email}\nPassword:{password}')
        # if is_correct:
        try:
            with open('password.json', 'r') as f:
                data = json.load(f)

        except FileNotFoundError:
            with open('password.json', 'w') as f:
                json.dump(new_data, f, indent=4)
        else:
            data.update(new_data)
            with open('password.json', 'w') as f:
                json.dump(data, f, indent=4)
        finally:
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #
root = tk.Tk()
root.title("MyPass")
root.config(padx=20, pady=20)
canvas = tk.Canvas(width=200, height=200)
canvas.grid(column=1, row=0, columnspan=2)
img = tk.PhotoImage(file="logo.png")
canvas.create_image(80, 80, image=img)

web_label = tk.Label(text="Website:")
web_label.grid(column=0, row=1)
website_entry = tk.Entry(width=38)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

email_label = tk.Label(text="Email:")
email_label.grid(column=0, row=2)
email_entry = tk.Entry(width=38)
email_entry.insert(0, 'lachowicz1991@protonmail.com')
email_entry.grid(column=1, row=2, columnspan=2)

password_label = tk.Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = tk.Entry(width=18)
password_entry.grid(column=1, row=3)

password_button = tk.Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3, sticky="w")

add_button = tk.Button(text="Add", width=35, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

root.mainloop()
