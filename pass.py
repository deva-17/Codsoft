import random
import string
import tkinter as tk
from tkinter import messagebox

def passwordgenerator():
    length = int(password_length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    generated_password_label.config(text="Password: " + password)

root = tk.Tk()
root.title("Password Generator")

title = tk.Label(root, text="PASSWORD GENERATOR", background="light yellow")
title.pack()

password_length_label = tk.Label(root, text="Enter the length of the password:")
password_length_label.pack()

password_length_entry = tk.Entry(root)
password_length_entry.pack()

generate_button = tk.Button(root, text="Generate ", command=passwordgenerator)
generate_button.pack()

generated_password_label = tk.Label(root, text="")
generated_password_label.pack()


root.mainloop()