from tkinter import *
from subprocess import call
from tkinter import messagebox
#from saving_test2 import login


root = Tk()

#root.maxsize(700,500)
#root.minsize(600,300)

def nextp1():
    call(["python", "saving_test2.py"])


def fakeclicks():
    call(["python","signin.py"])

def login_move():
    nextp1()
    #login()



lbl_1 = Label(root, text="WELCOME to CHAIN_BANK")
lbl_1.grid(row=0, column=0)

sign_in_button = Button(root, text="sign in", pady=20, padx=70, command=fakeclicks)
sign_in_button.grid(row=1, column=1)


sign_up_button = Button(root, text="sign up", pady=20, padx=70, command=nextp1)
sign_up_button.grid(row=1, column=2)


quit_button = Button(root, text="exit", padx=50, pady=30, command=quit)
quit_button.grid(row=2, column=3)
root.mainloop()