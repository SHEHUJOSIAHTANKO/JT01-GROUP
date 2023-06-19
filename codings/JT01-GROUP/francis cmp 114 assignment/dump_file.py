import tkinter as tk
from tkinter import messagebox

def check_age():
    age = int(age_entry.get())
    if age < 18:
        messagebox.showinfo("Not Eligible", "You are not eligible.")
    else:
        # Open another page or perform any other desired action
        messagebox.showinfo("Eligible", "You are eligible.")

# Create the main Tkinter window
window = tk.Tk()

# Create the age entry field
age_label = tk.Label(window, text="Age:")
age_label.pack()
age_entry = tk.Entry(window)
age_entry.pack()

# Create the submit button
submit_button = tk.Button(window, text="Submit", command=check_age)
submit_button.pack()

# Start the Tkinter event loop
window.mainloop()
