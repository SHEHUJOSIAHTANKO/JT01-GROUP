import tkinter as tk

def register_user():
    username = username_entry.get()
    password = password_entry.get()

    # Store the user in a database or file
    with open('users.txt', 'a') as file:
        file.write(f"{username}:{password}\n")

    # Clear the entry fields after registration
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

root = tk.Tk()

# Create entry fields for username and password
username_label = tk.Label(root, text="Username:")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Create a button to register the user
register_button = tk.Button(root, text="Register", command=register_user)
register_button.pack()

root.mainloop()
