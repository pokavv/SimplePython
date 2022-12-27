from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200) # config padding

# label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50) # label padding

# button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# new_button
new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

# entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)

window.mainloop()