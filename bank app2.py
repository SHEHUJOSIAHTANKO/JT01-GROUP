import tkinter as tk

class BankAccount:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance


class BankingAppGUI:
    def __init__(self):
        self.accounts = []

        self.window = tk.Tk()
        self.window.title("Banking App")

        self.label_account_number = tk.Label(self.window, text="Account Number:")
        self.label_account_number.pack()
        self.entry_account_number = tk.Entry(self.window)
        self.entry_account_number.pack()

        self.label_name = tk.Label(self.window, text="Name:")
        self.label_name.pack()
        self.entry_name = tk.Entry(self.window)
        self.entry_name.pack()

        self.label_balance = tk.Label(self.window, text="Balance:")
        self.label_balance.pack()
        self.entry_balance = tk.Entry(self.window)
        self.entry_balance.pack()

        self.button_create_account = tk.Button(self.window, text="Create Account", command=self.create_account)
        self.button_create_account.pack()

        self.label_account_action = tk.Label(self.window, text="Account Action:")
        self.label_account_action.pack()
        self.entry_account_action = tk.Entry(self.window)
        self.entry_account_action.pack()

        self.label_amount = tk.Label(self.window, text="Amount:")
        self.label_amount.pack()
        self.entry_amount = tk.Entry(self.window)
        self.entry_amount.pack()

        self.button_deposit = tk.Button(self.window, text="Deposit", command=self.deposit)
        self.button_deposit.pack()

        self.button_withdraw = tk.Button(self.window, text="Withdraw", command=self.withdraw)
        self.button_withdraw.pack()

        self.button_check_balance = tk.Button(self.window, text="Check Balance", command=self.check_balance)
        self.button_check_balance.pack()

    def create_account(self):
        account_number = self.entry_account_number.get()
        name = self.entry_name.get()
        balance = float(self.entry_balance.get())

        account = BankAccount(account_number, name, balance)
        self.accounts.append(account)

        print("Account created successfully.")

    def deposit(self):
        account_number = self.entry_account_action.get()
        amount = float(self.entry_amount.get())

        account = self.get_account(account_number)
        if account:
            account.deposit(amount)
            print("Deposit successful.")
        else:
            print("Account not found.")

    def withdraw(self):
        account_number = self.entry_account_action.get()
        amount = float(self.entry_amount.get())

        account = self.get_account(account_number)
        if account:
            account.withdraw(amount)
            print("Withdrawal successful.")
        else:
            print("Account not found.")

    def check_balance(self):
        account_number = self.entry_account_action.get()

        account = self.get_account(account_number)
        if account:
            balance = account.get_balance()
            print(f"Account balance: {balance}")
        else:
            print("Account not found.")

    def get_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def run(self):
        self.window.mainloop()

# Usage example
app = BankingAppGUI()
app.run()
