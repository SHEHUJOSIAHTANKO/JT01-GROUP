from tkinter import *
from subprocess import call
from tkinter import messagebox


def nextp1():
    call(["python", "main_page.py"])


##########################################

class BankAccount:
    def __init__(self, account_type):
        self.account_type = account_type
        self.balance = 2

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds.")

##########################

def open_accounts_window():
    name = sign_entry1.get()
    account_number = sign_entry2.get()
    age = int(age_entry1.get())
    if age < 18 and len(account_number) != 10:
        messagebox.showinfo("Incorrect account number"," Please enter a 10-digit account number, and you are not old enough to own an accountin this bank")

    else:
        accounts_window = Toplevel(root)
        accounts_window.title("Bank Accounts")

        name_label = Label(accounts_window, text=f"Welcome, {name}! Account Number: {account_number}")
        name_label.grid(row=0, column=0, columnspan=4)

        current_account = BankAccount("Current")
        savings_account = BankAccount("Savings")

        savings_balance = Label(accounts_window, text="Savings Account Balance: 0")
        savings_balance.grid(row=4, column=0)


        call(["python", "main_page.py"])



#################


def save_user_details():
    name = sign_entry1.get()
    account_number = sign_entry2.get()
    # Other details...

    # Store the user details in a file
    with open('user_details.txt', 'w') as file:
        file.write(f"Name: {name}\n")
        file.write(f"Account Number: {account_number}\n")


def combined_funts():
    open_accounts_window()
    save_user_details()



root= Tk()
root.title("chainBank")

#root.maxsize(800,500)
#root.minsize(600,300)


sign_label1 = Label(root, text="enter your name:")
sign_label1.grid(row=0, column=0)

sign_entry1 = Entry(root, width=35, borderwidth=5)
sign_entry1.grid(row=0, column=1)

sign_label2 = Label(root, text="enter your account number:")
sign_label2.grid(row=1, column=0)

sign_entry2 = Entry(root, width=35 , borderwidth=5)
sign_entry2.grid(row=1, column=1)



age_entry = Label(root, text="enter your Age:")
age_entry.grid(row=2, column=0)

age_entry1 = Entry(root, width=35 , borderwidth=5 )
age_entry1.grid(row=2, column=1)

sign_label_notice = Label(root, text="please do not disclose info!!!!!")
sign_label_notice.grid(row=3, column=1)



sign_button = Button(root, text="submit", pady=10, padx=70, command=combined_funts)
sign_button.grid(row=4, column=1)


button_quit = Button(root, text="exit program", command=root.quit)
button_quit.grid(row=5, column=5)
root.mainloop()

with open("data.txt", "w") as file:
    file.write(sign_entry1)

