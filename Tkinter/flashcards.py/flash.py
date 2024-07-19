from tkinter import *
import pandas as pd
import json 
from tkinter import messagebox
import random




data = pd.read_csv("Tkinter/flashcards.py/French Vocab.csv")
french_word = data.to_dict(orient='records')
#-------Generating french and english words------#
def french_words():
    current_word = random.choice(french_word)
    canvas.itemconfigure(card_title, text="French")
    canvas.itemconfigure(card_word, text=current_word['French'])
    def english_word():
        canvas.itemconfigure(card_title, text= "English")
        canvas.itemconfigure(card_word, text = current_word['English'])
        canvas.itemconfigure(card_front_photo, PhotoImage(file= "Tkinter/flashcards.py/flash-card-project-start/images/card_back.png"))
    window.after(3000,english_word)

def unknown_words():
    if wrong_button:
        with open("new_words.json", "w") as data_file:
            json.dump()


window = Tk()
window.title("Flassy")
window.config(padx=50, pady=50, bg="skyblue")

canvas = Canvas(width=800, height=526, bg="skyblue")
card_front_photo = PhotoImage(file="Tkinter/flashcards.py/flash-card-project-start/images/card_front.png")
card_back_photo = PhotoImage(file= "Tkinter/flashcards.py/flash-card-project-start/images/card_back.png")
image = canvas.create_image(400,263, image = card_front_photo)
card_title = canvas.create_text(400,150,text="Check", font=("Ariel", 40),fill="black")
card_word = canvas.create_text(400,263,text="",font=("Ariel", 40),fill="black")
canvas.config(bg="green", highlightthickness=0)
canvas.grid(column=0,row=0, columnspan=2)

#-----Buttons----#

my_image_right =PhotoImage(file="Tkinter/flashcards.py/flash-card-project-start/images/right.png")
right_button = Button(image= my_image_right, highlightthickness= 0, command= french_words)
right_button.grid(column= 1, row = 1)

my_image_wrong =PhotoImage(file="Tkinter/flashcards.py/flash-card-project-start/images/wrong.png")
wrong_button = Button(image= my_image_wrong, highlightthickness= 0, command= french_words)
wrong_button.grid(column=0, row=1)


french_words()

window.mainloop()
