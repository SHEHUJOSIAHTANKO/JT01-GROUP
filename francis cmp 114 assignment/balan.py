from tkinter import *
from subprocess import call
import pickle
root = Tk()

def check_balance():
    try:
        with open('account_balance.pkl', 'rb') as file:
            account_balance = pickle.load(file)
            balance_label.config(text=f"Account Balance: ${account_balance:.2f}")
    except FileNotFoundError:
        balance_label.config(text="Account Balance: N/A")


balance_label= Button(root,text="acc_balance", command=check_balance)
balance_label.grid(row=0, column=0)

button_quit = Button(root, text="exit program", pady=10, padx=80, command=root.quit)
button_quit.grid(row=5, column=3)

root.mainloop()