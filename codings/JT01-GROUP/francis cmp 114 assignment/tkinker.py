import tkinter as tk

def convert_fah_to_cel(self):
    fahrenheit = float(ent_fah.get())
    c=(float(5/9)*fahrenheit)-32
    print("your answer is:"+c)

window = tk.Tk()

window.title("fahrenheit to celcius")

frame = tk.Frame(master=window)
ent_fah = tk.Entry(master=frame, width=10)

lbl_fah = tk.Label(master=frame, text="\N{DEGREE FAHRENHEIT}")
lbl_fah.grid(row=0, column=0)
ent_fah = tk.Button(master=frame, text='click1')
ent_fah.grid(row=0, column=0)
btn_convert= tk.Button(master=frame, text="converter")


lbl_result = tk.label(master=frame, text="N\{DEGREE CELCIUS}")
btn_convert.grid(row=0, column=2)
btn_result.grid(row=0, column=2)
lbl_result['text'] = celsius, "\N{ DEGREE CELCIUS}"

window.mainloop()