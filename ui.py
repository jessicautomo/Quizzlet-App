from tkinter import *

THEME_COLOR = "#375362"


class UserInterface:

    def __innit__(self):
        self.window = Tk()
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0")
        self.score_label.grid(row=1, column=2)
        self.canvas = Canvas(width=300, height=250)
        self.text = self.canvas.create_text(150, 125, text="", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(row=2, column=1, columnspan=2)
        self.true_button = Button(image=true_img)
        self.true_button.grid(row=3, column=1)
        self.false_button = Button(image=false_img)
        self.true_button.grid(row=3, column=2)

    def update_score(self, score):
        self.score_label.config(text=f"Score: {score}")

    def change_question(self, question):
        self.canvas.itemconfig(self.text, text=f"{question}")

