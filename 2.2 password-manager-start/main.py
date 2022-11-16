import json
from tkinter import *
from tkinter import messagebox
import string
from random import randint, choice, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    upper_case = list(string.ascii_lowercase)
    lower_case = list(string.ascii_uppercase)
    numbers = list(string.digits)
    symbols = ['!', '#', '$', '&','*', '%', '+', '(', ')']

    password_uppercase = [choice(upper_case) for up in range(randint(1,3))]
    password_lowercase = [choice(lower_case) for low in range(randint(8, 10))]
    password_numbers = [choice(numbers) for num in range(randint(2,4))]
    password_symbols = [choice(symbols) for sym in range(randint(2,4))]

    password_list = password_uppercase+password_symbols+password_numbers+password_lowercase
    shuffle(password_list)
    password = ''.join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(END,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    new_data = {
        website_entry.get():{
            "email": email_entry.get(),
            "password": password_entry.get()
        }
    }

    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showwarning(title='Error', message='Required fields cannot be empty')
    else:
        message = messagebox.askokcancel(title=website_entry.get(), message=f'Details:\nEmail: {email_entry.get()}\n'
                                                                            f'Password: {password_entry.get()}\n Are you sure you'
                                                                            f'want to save?')
        if message:
            try:
                with open('vault.json', 'r') as data_file:
                    data = json.load(data_file)
                    data.update(new_data)

            except FileNotFoundError:
                with open('vault.json', 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                with open('vault.json', 'w') as data_file:
                    json.dump(data, data_file, indent=4)


            website_entry.delete(0, END)
            password_entry.delete(0, END)
            messagebox.showinfo(title='info', message ='Added Sucessfuly!' )

def search():
    if len(website_entry.get()) == 0:
        messagebox.showwarning(title='Error', message='Enter Website to search')
    else:
        try:
            with open('vault.json', 'r') as data_file:
                data = json.load(data_file)


        except FileNotFoundError:
            messagebox.showerror(title='Error', message=f"No records found for {website_entry.get()}")
        else:
            try:
                details = data[website_entry.get()]
            except KeyError:
                messagebox.showerror(title='Error', message=f"No records found for {website_entry.get()}")
            else:
                messagebox.showinfo(title=website_entry.get(), message=f"Email: {details['email']}\n"
                                                                       f"Password: {details['password']}")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file='logo.png')

canvas.create_image(100,100, image =lock_img)
canvas.grid(row=0, column=1)

website_label = Label(text='Website:')
website_label.grid(row=1, column=0)
email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)
password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

website_entry = Entry(width=32)
website_entry.focus()
website_entry.grid(row=1, column=1)
email_entry = Entry(width=50)
email_entry.insert(END, 'yuguda999@gmail.com')
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text = 'Generate Password',width= 14, command= generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text= 'Add', width=42, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text = 'Search', width = 13, command=search)
search_button.grid(row=1, column=2)
window.mainloop()