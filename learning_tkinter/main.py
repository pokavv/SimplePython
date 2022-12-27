import tkinter as tk

# create tkinter window
window = tk.Tk()
window.title('GUI test')
window.minsize(width=500, height=400)

# grid(column=1, row=1) 
# grid(): row와 column으로 위치 설정, 앞줄에 설정된 grid()가 없으면 자리채움

# label
my_label = tk.Label(text='Hello World', font=('Arial', 24, 'italic'))
my_label.pack()

my_label['text'] = '안녕하세요'
my_label.config(text='안녕하세요')

# button
def click_event():
    print('click')
    new_text = input.get()
    my_label.config(text=new_text)

btn = tk.Button(text='Click Me', command=click_event)
btn.pack()

# entry
input = tk.Entry(width=30)
input.insert(tk.END, string='Some text to begin with.')
print(input.get())
input.pack()

# text
text = tk.Text(height=5, width=30)
text.focus()
text.insert(tk.END, 'Example of multi-line text entry.')
print(text.get('1.0', tk.END))
text.pack()

# spinbox
def spinbox_used():
    print(spinbox.get())

spinbox = tk.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# scale
def scale_used(value):
    print(value)

scale = tk.Scale(from_=0, to=100, command=scale_used)
scale.pack()

# checkbutton
def checkbtn_used():
    print(chk_state.get())

chk_state = tk.IntVar()
chk_btn = tk.Checkbutton(text='체크할거야?', variable=chk_state, command=checkbtn_used)
chk_state.get()
chk_btn.place(x=30, y=100) # place(): pack() method보다 더 정교하게 조정가능

# radiobutton
def radio_used():
    print(radio_state.get())

radio_state = tk.IntVar()
radiobtn1 = tk.Radiobutton(text='눌러', value=1, variable=radio_state, command=radio_used)
radiobtn2 = tk.Radiobutton(text='눌러', value=2, variable=radio_state, command=radio_used)
radiobtn1.pack()
radiobtn2.pack()

# listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = tk.Listbox(height=4)
animals = ['tiger', 'shark', 'killer whale', 'dog', 'puma']
for animal in animals:
    listbox.insert(animals.index(animal), animal)
listbox.bind('<<ListboxSelect>>', listbox_used)
listbox.pack()

window.mainloop()