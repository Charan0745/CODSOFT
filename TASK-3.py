# Password Generator
import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    
    if length <= 0:
        password_label.config(text="Invalid length")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    password_label.config(text="Generated Password:")

window = tk.Tk()
window.title("Random Password Generator")
window.geometry("300x300")

length_label = tk.Label(window, text="Enter Password Length:")
length_label.pack(pady=10)

length_entry = tk.Entry(window, width=10, justify="center")
length_entry.pack(pady=5)

generate_button = tk.Button(window, text="Generate Random Password", command=generate_password)
generate_button.pack(pady=10)

password_label = tk.Label(window, text="")
password_label.pack()

password_entry = tk.Entry(window, width=30, justify="center")
password_entry.pack(pady=5)

window.mainloop()
