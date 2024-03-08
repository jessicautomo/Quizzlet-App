from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from tkinter import *

THEME_COLOR = "#375362"

window = Tk()
true_img = PhotoImage(file="images/true.png")
false_img = PhotoImage(file="images/false.png")
window.title("Quizzler")
window.config(padx=20, pady=20, bg=THEME_COLOR)
score_label = Label(text="Score: 0",bg=THEME_COLOR,fg="white")
score_label.grid(row=1, column=2)
canvas = Canvas(width=300, height=250,highlightcolor=THEME_COLOR,highlightthickness=10)
text = canvas.create_text(150, 125, width = 260,text="", fill=THEME_COLOR, font=("Arial", 15, "italic"))
canvas.grid(row=2, column=1, columnspan=2)
true_button = Button(image=true_img)
true_button.grid(row=3, column=1)
false_button = Button(image=false_img)
false_button.grid(row=3, column=2)

def update_score(score):
    score_label.config(text=f"Score: {score}")

def change_question(question):
    canvas.itemconfig(text, text=f"{question}", fill=THEME_COLOR)


question_bank = []

for question in question_data["results"]:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

def end():
    canvas.itemconfig(text,text=f"You've completed the quiz!\nYour final score was: {quiz.score}/{quiz.question_number}")

def next_question():
    quiz.next_question()
    change_question(quiz.q_text)
    if quiz.current_question.answer.lower() == "true":
        text_color = "green"
    else:
        text_color = "red"

    def next():
        if quiz.still_has_questions():
            next_question()
        else:
            end()

    def true_clicked():
        true_button.config(command=None)
        user_answer = "True"
        quiz.check_answer(user_answer)
        update_score(quiz.score)
        canvas.itemconfig(text, text=f"{quiz.current_question.answer}", fill=text_color)
        window.after(3000, next)


    true_button.config(command=true_clicked)


    def false_clicked():
        false_button.config(command=None)
        user_answer = "False"
        quiz.check_answer(user_answer)
        update_score(quiz.score)
        canvas.itemconfig(text, text=f"{quiz.current_question.answer}", fill=text_color)
        window.after(3000, next)


    false_button.config(command=false_clicked)

next_question()


window.mainloop()