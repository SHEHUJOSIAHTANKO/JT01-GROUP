import tkinter as tk

root = tk.Tk()
root.geometry('600x400')
root.title('tkinter hub')

options_frame = tk.Frame(root, bg='#c5r5c5')



options_frame.pack(side=tk.LEFT )
options_frame.pack_propagate(False)
options_frame.configure(width=200, height=600)

main_frame = tk.Frame(root, highlightbackground='black', highlightthickness=8)

main_frame.pack(side=tk.LEFT
                )
main_frame.pack_propagate(False)
main_frame.configure(height=700, width=600)

root.mainloop()

