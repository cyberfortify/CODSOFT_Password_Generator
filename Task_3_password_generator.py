import tkinter as tk
import string
import random

# Function to generate the password
def generate_password():
    try:
        length = int(length_entry.get())
        
        if length <= 0:
            password_label.config(text=("Error!!! Password length must be a positive integer."))
            return
        
        characters = string.ascii_letters + string.digits + string.punctuation
        
        # Generate the password
        password = " ".join(random.sample(characters,length))
        
        # Display the generated password
        password_label.config(text=f'The Generated Password is:  {password}')
    
    except ValueError:
        password_label.config(text="Error!!!   Please enter a valid number.")

root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Enter the desired length for your password:")
length_label.pack(pady=10)

length_entry = tk.Entry(root, bd=4, borderwidth=2)
length_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

password_label = tk.Label(root, text=" ", font=("Helvetica", 12, "bold"))
password_label.pack(pady=10)

root.mainloop()
