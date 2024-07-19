from tkinter import *

window =Tk()


window.title("My First GUI program")
window.minsize(width=500, height = 500)

def button_clicked():
    new_text = input.get()
    my_label.config(text =new_text)

my_label = Label(text=" Created a label", font=("Times New Roman", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

new_button = Button(text="New Button")
new_button.grid(column=2, row= 0)

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row= 1)

input = Entry(width=12)
print(input.get())
input.grid(column=3, row=2)








window.mainloop()