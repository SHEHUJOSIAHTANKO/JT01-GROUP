from tkinter import *
from tkinter import messagebox

class SavingsAccountGUI:
    def __init__(self, master):
        self.master = master
        master.title("Savings Account")

        self.balance = 0

        self.balance_label = Label(master, text="Balance: #0")
        self.balance_label.pack()

        self.deposit_label = Label(master, text="Deposit Amount:")
        self.deposit_label.pack()

        self.deposit_entry = Entry(master)
        self.deposit_entry.pack()

        self.deposit_button = Button(master, text="Deposit", command=self.deposit)
        self.deposit_button.pack()

        self.withdraw_label = Label(master, text="Withdraw Amount:")
        self.withdraw_label.pack()

        self.withdraw_entry = Entry(master)
        self.withdraw_entry.pack()

        self.withdraw_button = Button(master, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack()

        self.quit_button = Button(master, text="Quit", command=master.quit)
        self.quit_button.pack()


    def deposit(self):
        amount = float(self.deposit_entry.get())
        self.balance += amount
        self.update_balance()

    def withdraw(self):
        amount = float(self.withdraw_entry.get())
        if amount <= self.balance:
            self.balance -= amount
            self.update_balance()
        else:
            messagebox.showerror("Error", "Insufficient funds")


    def update_balance(self):
        self.balance_label.config(text="Balance: #" + str(self.balance))
        self.deposit_entry.delete(0, END)
        self.withdraw_entry.delete(0, END)


root = Tk()
gui = SavingsAccountGUI(root)
root.mainloop()        
