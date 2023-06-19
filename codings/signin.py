from tkinter import *




def login():
    # Retrieve user input from entry fields
    username = username_entry.get()
    password = pin_entry1.get()
    account_number = sign_entry2

    # Check if the username and password match an existing account
    with open('accounts.txt', 'r') as file:
        for line in file:
            account_info = line.strip().split(':')
            if account_info[0] == username and account_info[1] == password:
                account_number = float(account_info[2])
                show_login(account_number)
                return

    # Clear the entry fields after login attempt
    username_entry.delete(0, END)
    pin_entry1.delete(0, END)
    sign_entry2.delete(0, END)


def show_login():
    # Clear the entry fields and message label
    username_entry.delete(0, END)
    pin_entry1.delete(0, END)
    sign_entry2.delete(0, END)

    # Hide the login and create account widgets
    sign_label1.pack_forget()
    username_entry.pack_forget()
    pin_entry.pack_forget()
    pin_entry1.pack_forget()


root = Tk()


sign_label1 = Label(root, text="username:")
sign_label1.grid(row=0, column=0)

username_entry = Entry(root, width=35, borderwidth=5)
username_entry.grid(row=0, column=1)

sign_label2 = Label(root, text="account number:")
sign_label2.grid(row=1, column=0)

sign_entry2 = Entry(root, width=35 , borderwidth=5, show="*")
sign_entry2.grid(row=1, column=1)



pin_entry = Label(root, text="pin:")
pin_entry.grid(row=2, column=0)

pin_entry1 = Entry(root, width=35 , borderwidth=5, show="*")
pin_entry1.grid(row=2, column=1)

sign_label_notice = Label(root, text="please do not disclose info!!!!!")
sign_label_notice.grid(row=3, column=1)



sign_button = Button(root, text="submit", pady=10, padx=80, command=login)
sign_button.grid(row=4, column=1)


button_quit = Button(root, text="exit program", command=root.quit)
button_quit.grid(row=5, column=5)

root.mainloop()


