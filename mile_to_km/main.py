from tkinter import *

def convert_to_km():
    miles = float(mile.get())
    km = miles * 1.609
    result_label.config(text=f'{km}')

window = Tk()
window.title('Miles to Kilometer')
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

mile = Entry(width=7)
mile.grid(column=1, row=0)

miles_label = Label(text='Miles')
miles_label.grid(column=2, row=0)

is_equal_label = Label(text='is equal to')
is_equal_label.grid(column=0, row=1)

result_label = Label(text='0')
result_label.grid(column=1, row=1)

km_label = Label(text='km')
km_label.grid(column=2, row=1)

convert_button = Button(text='Convert', command=convert_to_km)
convert_button.grid(column=1, row=2)

window.mainloop()