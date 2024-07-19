from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

#------Generate Password----#
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters+password_symbols+password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_text.insert(0,password)
#-------Save Password-----#
def added():

    website = web_text.get()
    email = email_text.get()
    password = password_text.get()
    new_data = {
        website : {
            "email" : email,
            "password": password,

        } 
          }
   
    if(len(website)==0) or len(password)==0:
        messagebox.askretrycancel(title="Oops", message="You left fields empty please fill again ")
    else:
        try:
            with open("data.json","r") as data_file:
                data =json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json","w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_text.delete(0,END)
            password_text.delete(0,END)

#-----Find Password -----#
def find_password():
    try:
        website = web_text.get()
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data found")
    else:
        if website in data:
            email = data[website][email]
            password = password[website]["password"]
            messagebox.showinfo(title=website, message= f"email:{email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No Information found for {website}")
            
#------User Interface-------#

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="/Users/User/Downloads/pomodoro-start/password_/Lock.png")
canvas.create_image(100,100, image = photo)
canvas.grid(column=1,row=0)

website = Label(text="Website :")
website.grid(column=0, row=1)

web_text= Entry(width=21)
web_text.grid(column=1,row=1)

email = Label(text="Email/Username:")
email.grid(column=0,row=2)

email_text = Entry(width=35)
email_text.grid(column=1, row= 2,columnspan=2)
email_text.insert(0,"example@gmail.com")

password = Label(text="Password:")
password.grid(column=0,row=3)

password_text = Entry(width=21)
password_text.grid(column=1, row= 3)

search_button = Button(text="Search",width ="14",command=find_password)
search_button.grid(column=2, row=1)

password_button = Button(text="Generate password", command=generate_password)
password_button.grid(column=2, row= 3)

add_button = Button(text="Add",width=35, command=added)
add_button.grid(column=1, row =4,columnspan=2)


window.mainloop()