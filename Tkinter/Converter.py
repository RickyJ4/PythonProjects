from tkinter import *

window =Tk()

window.title("Miles to Km Converter")
window.minsize(width=300, height = 400)

def converter():
    new_text = float(input.get())
    new_text = int(new_text * 1.60934)
    second_label.config(text = new_text)

first_label = Label(text=" is equal to", font=("Times New Roman", 24, "bold"))
first_label.grid(column=0, row= 2)
first_label.config(padx=20,pady=20)

second_label = Label(text=" 0 ", font=("Times New Roman", 24, "bold"))
second_label.grid(column=2, row= 2)
second_label.config(padx=20,pady=20)

third_label = Label(text=" Km ", font=("Times New Roman", 24, "bold"))
third_label.grid(column=3, row= 2)
third_label.config(padx=20,pady=20)

fourth_label = Label(text=" Miles", font=("Times New Roman", 24, "bold"))
fourth_label.grid(column=3, row= 0)
fourth_label.config(padx=20,pady=20)

button =Button(text="Calculate" , command= converter)
button.grid(column=2, row=3)

input = Entry(width=12)
print(input.get())
input.grid(column=2, row=0)









window.mainloop()