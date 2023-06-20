import tkinter as tk

window = tk.Tk()
window.title("fahrenheit to Celsius")
window.geometry("800x500")

frame = tk.Frame(master=window)
ent_fah = tk.Entry(master=frame, width=10)
lbl_fah = tk.Label(master=frame, text="\N{DEGREE FAHRENHEIT}")

lbl_result = tk.Label(master=frame, text="\N{DEGREE CELSIUS}")
frame.grid(row=1, column=1)


# Always Remember to put function after input

def convert_fah_to_cel():
    fah = float(ent_fah.get())
    celsius = ((5 / 9) * (fah - 32))
    print(celsius)
    lbl_result['text'] = round(celsius, 2), "\N{DEGREE CELSIUS}"  # To show the results on the gui


btn_convert = tk.Button(master=frame, command=convert_fah_to_cel, text="Convert")

ent_fah.grid(row=0, column=0)
lbl_fah.grid(row=0, column=1)
btn_convert.grid(row=1, column=0)
lbl_result.grid(row=1, column=1)
# Rows and column determine arrangement of elements of function
window.mainloop()
