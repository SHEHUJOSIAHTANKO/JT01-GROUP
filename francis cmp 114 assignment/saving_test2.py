from tkinter import *
from subprocess import call
from tkinter import messagebox



##########################################

class BankAccount:
    def __init__(self, account_type):
        self.account_type = account_type
        self.balance = 1

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds.")

##########################

def open_accounts_window():
    name = username_entry.get()
    account_number = sign_entry2.get()
    pin = int(pin_entry1.get())
    if pin != 8 and len(account_number) != 10:
        messagebox.showinfo("Incorrect account number"," Please enter a 10-digit account number, and your  pin should be longer ")

    else:
        accounts_window = Toplevel(root)
        accounts_window.title("Bank Accounts")

        name_label = Label(accounts_window, text=f"Welcome, {name}! Account Number: {account_number}")
        name_label.grid(row=0, column=0, columnspan=4)

        current_account = BankAccount("Current")
        savings_account = BankAccount("Savings")

        savings_balance = Label(accounts_window, text="Savings Account Balance: 0")
        savings_balance.grid(row=4, column=0)


        call(["python", "saving_test3.py"])



#################


def save_user_details():
    name = username_entry.get()
    account_number = sign_entry2.get()
    # Other details...

    # Store the user details in a file
    with open('user_details.txt', 'w') as file:
        file.write(f"Name: {name}\n")
        file.write(f"Account Number: {account_number}\n")


def combined_funts():
    open_accounts_window()
    save_user_details()
    create_account()
########################################

def create_account():
    # Retrieve user input from entry fields
    username = username_entry.get()
    password = pin_entry1.get()
    acc_number = float(sign_entry2.get())

    # Store the account details in a database or file
    with open('accounts.txt', 'a') as file:
        file.write(f"{username}:{password}:{acc_number}\n")

    # Clear the entry fields after creating the account
    username_entry.delete(0, END)
    pin_entry1.delete(0, END)
    sign_entry2.delete(0, END)
    
    
def login():
    # Retrieve user input from entry fields
    username = username_entry.get()
    password = pin_entry1.get()

    # Check if the username and password match an existing account
    with open('accounts.txt', 'r') as file:
        for line in file:
            account_info = line.strip().split(':')
            if account_info[0] == username and account_info[1] == password:
                account_balance = float(account_info[2])
               # show_balance(account_balance)
                return

    # Clear the entry fields after login attempt
    username_entry.delete(0, END)
    pin_entry1.delete(0, END)

    # Display an error message for unsuccessful login
    #message_label.config(text="Invalid username or password", fg="red")


def show_balance(balance):
    # Clear the entry fields and message label
    username_entry.delete(0, END)
    pin_entry1.delete(0, END)


    # Hide the login and create account widgets
    sign_label1.pack_forget()
    username_entry.pack_forget()
    pin_entry.pack_forget()
    pin_entry1.pack_forget()





###########################################################

def recall():
    open_accounts_window()
    save_user_details()
    create_account()
    login()
########################################
root = Tk()
root.title("chainBank")

#root.maxsize(700,500)
#root.minsize(600,300)


sign_label1 = Label(root, text="enter your name:")
sign_label1.grid(row=0, column=0)

username_entry = Entry(root, width=35, borderwidth=5)
username_entry.grid(row=0, column=1)

sign_label2 = Label(root, text="enter your account number:")
sign_label2.grid(row=1, column=0)

sign_entry2 = Entry(root, width=35 , borderwidth=5, show="*")
sign_entry2.grid(row=1, column=1)



pin_entry = Label(root, text="password:")
pin_entry.grid(row=2, column=0)

pin_entry1 = Entry(root, width=35 , borderwidth=5, show="*")
pin_entry1.grid(row=2, column=1)

sign_label_notice = Label(root, text="please do not disclose info!!!!!")
sign_label_notice.grid(row=3, column=1)



sign_button = Button(root, text="submit", pady=10, padx=80, command=recall)
sign_button.grid(row=4, column=1)



button_quit = Button(root, text="exit program", command=root.quit)
button_quit.grid(row=5, column=5)

root.mainloop()

with open("data.txt", "w") as file:
    file.write(username_entry)

