import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
SCORE_LABEL_FONT = ("Ariel", 14, "normal")
QUESTION_FONT = ("Ariel", 20, "italic")


class QuizUi:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tk.Tk()
        self.window.title("Quizler")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        # Question canvas
        self.canvas = tk.Canvas(width=300, height=250, background="white")
        self.canvas.config()
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.question_text = self.canvas.create_text(150, 125, text="", font=QUESTION_FONT, width=280)

        # Labels
        self.score = self.score_label = tk.Label(
            text=f"Score: {self.quiz.score}",
            font=SCORE_LABEL_FONT,
            foreground="white",
            background=THEME_COLOR
        )
        self.score_label.grid(row=0, column=1)

        # Buttons
        true_button_img = tk.PhotoImage(file="images/true.png")
        self.true_button = tk.Button(
            image=true_button_img,
            padx=20,
            pady=20,
            borderwidth=0,
            command=self.user_answers_true
        )
        self.true_button.grid(row=2, column=0, padx=20, pady=20)
        false_button_img = tk.PhotoImage(file="images/false.png")
        self.false_button = tk.Button(
            image=false_button_img,
            padx=20, pady=20,
            borderwidth=0,
            command=self.user_answers_false
        )
        self.false_button.grid(row=2, column=1, padx=20, pady=20)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        next_question_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=next_question_text)

    def user_answers_true(self):
        self.quiz.check_answer(user_answer="True")

    def user_answers_false(self):
        self.quiz.check_answer(user_answer="False")
