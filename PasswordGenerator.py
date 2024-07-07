import tkinter as tk
from tkinter import StringVar
import random
import string

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        master.title("Password Generator")

        # Label
        self.label = tk.Label(master, text="Password Length:")
        self.label.pack(pady=10)

        # Password length wanted
        self.length = tk.Entry(master)
        self.length.pack()

        # Button for generate password
        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=5)

        # Display generated password
        self.password = StringVar()
        self.password_display = tk.Entry(master, textvariable=self.password, state='readonly', width=35)
        self.password_display.pack()
        

    def generate_password(self):
        length = int(self.length.get())
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        self.password.set(password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()