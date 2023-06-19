from tkinter import *
import pickle


root = Tk()
account_balance = 0

def save_money():
    amount = float(savings_entry.get())
    with open('account_balance.pkl', 'wb') as file:
        pickle.dump(amount, file)


def save_user_details():
    depository= error_label.get()
    # Other details...

    # Store the user details in a file
    with open('user_details.txt', 'w') as file:
        file.write(f"Name: {depository}\n")
def depository():
    global account_balance
    amount = float(savings_entry.get())
    account_balance += amount
    update_bal()

def comi_Functs():
    depository()
    save_money()
def with_amount():
    global account_balance
    amount = float(savings_entry.get())
    if amount <= account_balance:
        account_balance -= amount
        update_bal()
    else:
        # Handle insufficient balance error
        error_label.config(text="Insufficient balance.")

def update_bal():
    savings_balance.config(text=f"Account Balance: ${account_balance:.2g}")


savings_label = Label(root, text="Savings Account",)
savings_label.grid(row=3, column=0)

savings_entry = Entry(root, width=35, borderwidth=5)
savings_entry.grid(row=3, column=1)

savings_dep = Button(root, text="Deposit",padx=80, pady=20,  command=comi_Functs)
savings_dep.grid(row=3, column=2)

savings_with = Button(root, text="Withdraw", padx=80, pady=20, command=with_amount)
savings_with.grid(row=4, column=2)


button_quit = Button(root, text="exit program", pady=10, padx=80, command=root.quit)
button_quit.grid(row=5, column=3)


savings_balance = Label(root, text="Savings Account Balance: 0")
savings_balance.grid(row=4, column=0)

error_label = Label(root, text="")
error_label.grid(row=6, column=4)

root.mainloop()