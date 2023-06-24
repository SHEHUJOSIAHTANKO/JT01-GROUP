import tkinter as tk
from tkinter import messagebox

class SavingsAccountGUI:
    def __init__(self):
        self.balance = 0

        self.window = tk.Tk()
        self.window.title("Savings Account")
        
        self.label = tk.Label(self.window, text="Current Balance: #0")
        self.label.pack()

        self.deposit_entry = tk.Entry(self.window)
        self.deposit_entry.pack()
        
        self.deposit_button = tk.Button(self.window, text="Deposit", command=self.deposit)
        self.deposit_button.pack()

        self.withdraw_entry = tk.Entry(self.window)
        self.withdraw_entry.pack()
        
        self.withdraw_button = tk.Button(self.window, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack()

        self.window.mainloop()

    def update_balance_label(self):
        self.label["text"] = f"Current Balance: ${self.balance}"

    def deposit(self):
        try:
            amount = float(self.deposit_entry.get())
            if amount <= 0:
                raise ValueError
            self.balance += amount
            self.update_balance_label()
            messagebox.showinfo("Success", "Deposit successful.")
            self.deposit_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Invalid deposit amount.")

    def withdraw(self):
        try:
            amount = float(self.withdraw_entry.get())
            if amount <= 0 or amount > self.balance:
                raise ValueError
            self.balance -= amount
            self.update_balance_label()
            messagebox.showinfo("Success", "Withdrawal successful.")
            self.withdraw_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Invalid withdrawal amount or insufficient funds.")

if __name__ == "__main__":
    savings_account = SavingsAccountGUI()
