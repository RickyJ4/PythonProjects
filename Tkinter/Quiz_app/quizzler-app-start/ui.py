from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx= 20, pady= 20, bg=THEME_COLOR)

        self.score = Label(text="score : 0", fg= "white")
        self.score.grid(column=1, row=0, bg = THEME_COLOR)

        self.canvas = Canvas(width=300, height= 250, bg= "white")
        self.questions = self.canvas.create_text(150,125,text="Questions", fill= THEME_COLOR, font=("Ariel"))
        self.canvas.grid(row=1,column=0,columnspan=2)

        self.right_button = Button()




        self.window.mainloop()
