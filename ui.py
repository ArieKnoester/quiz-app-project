import tkinter as tk
THEME_COLOR = "#375362"
SCORE_LABEL_FONT = ("Ariel", 14, "normal")
QUESTION_FONT = ("Ariel", 20, "italic")


class QuizUi():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quizler")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)
        self.score = 0

        # Question canvas
        self.canvas = tk.Canvas(width=300, height=250, background="white")
        self.canvas.config()
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.question_text = self.canvas.create_text(150, 125, text="STUFF", font=QUESTION_FONT)

        # Labels
        self.score_label = tk.Label(text=f"Score: {self.score}", font=SCORE_LABEL_FONT, foreground="white", background=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Buttons
        true_button_img = tk.PhotoImage(file="images/true.png")
        self.true_button = tk.Button(image=true_button_img, padx=20, pady=20, borderwidth=0)
        self.true_button.grid(row=2, column=0, padx=20, pady=20)
        false_button_img = tk.PhotoImage(file="images/false.png")
        self.false_button = tk.Button(image=false_button_img, padx=20, pady=20, borderwidth=0)
        self.false_button.grid(row=2, column=1, padx=20, pady=20)
        self.window.mainloop()
