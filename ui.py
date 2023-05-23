from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WHITE = "#FFFFFF"
FONT = ("Arial", 20, "italic")

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain ):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.label = Label(text="Score: 0", background=THEME_COLOR, fg=WHITE)
        self.label.grid(row=0, column=2)

        self.canvas = Canvas(width=300, height=250, bg=WHITE, highlightthickness=0)
        self.question_text = self.canvas.create_text((150, 125), width=280, text="Hello", fill=THEME_COLOR, font=FONT)
        self.canvas.grid(row=1, column=1, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.true_btn = Button(image= true_img, highlightthickness=0)
        self.true_btn.grid(row=2, column=1,  padx=20)
        self.false_btn = Button(image=false_img, highlightthickness=0)
        self.false_btn.grid(row=2, column=2, padx=20)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

