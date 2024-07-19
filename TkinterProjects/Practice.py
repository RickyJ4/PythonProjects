from tkinter import *
from tkinter import ttk

def update_label(number):
    current_text = label.cget('text')
    new_text = current_text +str(number)
    label.configure(text=new_text)

root = Tk()
root.title('Basic Calculator')
root.geometry('350x150')

mainframe = ttk.Frame(root, padding= '3 3 12 12')
mainframe.grid(column=0, row=0, sticky=(N, E, S, W))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

num_input = StringVar()


label = ttk.Label(mainframe, text='0')
label.grid(columnspan=4,row=0, sticky=W)


ttk.Button(mainframe, text= '9', width=5, command=lambda:update_label(9)).grid(column=1, row=1)
ttk.Button(mainframe, text= '8', width=5, command=lambda: update_label(8)).grid(column=2, row=1)
ttk.Button(mainframe, text= '7', width=5, command=lambda:update_label(7)).grid(column=3, row=1)

ttk.Button(mainframe, text= '6', width=5, command=lambda: update_label(6)).grid(column=1, row=2)
ttk.Button(mainframe, text= '5', width=5, command=lambda: update_label(5)).grid(column=2, row=2)
ttk.Button(mainframe, text= '4', width=5, command=lambda: update_label(4)).grid(column=3, row=2)

ttk.Button(mainframe, text= '3', width=5, command=lambda: update_label(3)).grid(column=1, row=3)
ttk.Button(mainframe, text= '2', width=5, command=lambda: update_label(2)).grid(column=2, row=3)
ttk.Button(mainframe, text= '1', width=5, command=lambda: update_label(1)).grid(column=3, row=3)

ttk.Button(mainframe, text= '', width=5, command=lambda:update_label(0)).grid(column=1, row=4)
ttk.Button(mainframe, text= '.', width=5, command=lambda:update_label).grid(column=2, row=4)
ttk.Button(mainframe, text= '=', width=5, command=update_label).grid(column=3, row=4)

ttk.Button(mainframe, text= '+', width=5, command=update_label).grid(column=4, row=1)
ttk.Button(mainframe, text= '/', width=5, command=update_label).grid(column=4, row=2)
ttk.Button(mainframe, text= '*', width=5, command=update_label).grid(column=4, row=3)
ttk.Button(mainframe, text= '-', width=5, command=update_label).grid(column=4, row=4)

root.mainloop()



