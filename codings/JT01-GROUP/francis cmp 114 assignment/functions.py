def show_balance(balance):
    # Clear the entry fields and message label
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    message_label.config(text="")

    # Hide the login and create account widgets
    username_label.pack_forget()
    username_entry.pack_forget()
    password_label.pack_forget()
    password_entry.pack_forget()
    create_button.pack_forget()
    login_button.pack_forget()

    # Display the account balance
    balance_label.config(text=f"Account Balance: ${balance:.2g}", fg="blue")
    balance_label.pack()

def check_balance():
    try:
        with open('account_balance.pkl', 'rb') as file:
            account_balance = pickle.load(file)
            balance_label.config(text=f"Account Balance: ${account_balance:.2g}")
    except FileNotFoundError:
        balance_label.config(text="Account Balance: N/A")



def nextp11():
    call(["python", "acc_det.py"])

def nextp1():
    call(["python", "savings.py"])

def display_account_detailes():
    # Read the user details from the file
    with open('user_details.txt', 'r') as file:
        user_details = file.read()

    # Display the user details
    account_balance_window = Toplevel(root)
    details_label = Label(account_balance_window, text=user_details)
    details_label.pack()

def display_account_balance():
    # Read the user details from the file
    with open('user_details.txt', 'r') as file:
        user_details = file.read()

    # Display the user details
    account_balance_window = Toplevel(root)
    details_label = Label(account_balance_window, text=user_details)
    details_label.pack()




def combined2():
    display_account_balance()

def nextp2():
    call(["python","balan.py"])



def combined_funts():
    display_account_detailes()




def nextp1():
    call(["python", "saving_test2.py"])


def fakeclicks():
    call(["python","saving_test2.py"])


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
    name = username_entry.get()
    account_number = sign_entry2.get()
    pin = int(pin_entry1.get())
    if pin != 8 and len(account_number) != 10:
        messagebox.showinfo("Incorrect account number",
                            " Please enter a 10-digit account number, and you are pin should be longer ")

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
    # message_label.config(text="Invalid username or password", fg="red")


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
    create_account()
    combined_funts()

########################################