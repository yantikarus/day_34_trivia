from tkinter import *
THEME_COLOR = "#375362"
WHITE = "#FFFFFF"
FONT = ("Arial", 20, "italic")

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg=WHITE, highlightthickness=0)
        self.canvas.grid(row=1, column=1, columnspan=2)
        self.text = self.canvas.create_text((150, 150), text="Hello", fill='black', font=FONT)
        self.true_img = PhotoImage(file="images/true.png")
        self.false_img = PhotoImage(file="images/false.png")
        self.true_btn= Button(image= self.true_img)
        self.true_btn.grid(row=2, column=1)
        self.false_btn = Button(image=self.false_img)
        self.false_btn.grid(row=2, column=2)

        self.window.mainloop()

