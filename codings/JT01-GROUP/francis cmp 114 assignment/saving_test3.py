from tkinter import *
from subprocess import call
import pickle

root= Tk()

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

root.title("chain-Bank")

#root.maxsize(700,500)
#root.minsize(600,300)

bank_text = Label(root, text= "available services:" )
bank_text.grid(row=0, column=1)

savings_b = Button(root, text="savings", padx=80, pady=20, command=nextp1)
savings_b.grid(row=1, column=1)

savings_b = Button(root, text="Balance", padx=80, pady=20, command=nextp2)
savings_b.grid(row=2, column=1)

savings_b = Button(root, text="account details", padx=80, pady=20, command=combined_funts)
savings_b.grid(row=3, column=1)

savings_b = Button(root, text="transfers", padx=70, pady=20, command=nextp11)
savings_b.grid(row=4, column=1)

button_quit = Button(root, text="exit program", command=root.quit)
button_quit.grid(row=5, column=5)
root.mainloop()