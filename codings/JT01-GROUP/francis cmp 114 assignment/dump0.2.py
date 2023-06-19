import tkinter as tk

# Create the main Tkinter window
window = tk.Tk()

# Create a label to display the account balance
balance_label = tk.Label(window, text="Account Balance: $0.00")
balance_label.pack()

def open_second_page(balance):
    # Create a new window for the second page
    second_window = tk.Toplevel(window)

    # Create a label in the second page to display the account balance
    second_balance_label = tk.Label(second_window, text=f"Account Balance: ${balance:.2f}")
    second_balance_label.pack()

# Function to retrieve the account balance and open the second page
def check_balance():
    account_balance = 1000  # Replace with your account balance retrieval logic
    open_second_page(account_balance)

# Create a button to check the balance
balance_button = tk.Button(window, text="Check Balance", command=check_balance)
balance_button.pack()

# Start the Tkinter event loop
window.mainloop()
