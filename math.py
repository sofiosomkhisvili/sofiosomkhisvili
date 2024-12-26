import tkinter as tk
import random
from tkinter import messagebox

class MathApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Math App")

        self.current_question = None
        self.correct_answer = None

        # Create main frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(pady=20)

        # Label for displaying the math problem
        self.problem_label = tk.Label(self.main_frame, text="", font=("Arial", 16))
        self.problem_label.pack(pady=10)

        # Label for prompt
        self.prompt_label = tk.Label(self.main_frame, text="გამოიანგარიშე", font=("Arial", 14))
        self.prompt_label.pack(pady=5)

        # Input for the user's answer
        self.answer_input = tk.Entry(self.main_frame, font=("Arial", 14))
        self.answer_input.pack(pady=10)
        self.answer_input.bind("<KeyRelease>", self.check_answer)
        self.answer_input.focus()

        # Label for feedback
        self.feedback_label = tk.Label(self.main_frame, text="", font=("Arial", 16))
        self.feedback_label.pack(pady=10)

        self.generate_question()

    def generate_question(self):
        self.feedback_label.config(text="")
        self.answer_input.delete(0, tk.END)

        operations = ['+', '-', '*', '/']
        operation = random.choice(operations)
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)

        if operation == '+':
            while num1 + num2 > 100:
                num1, num2 = random.randint(1, 100), random.randint(1, 100)
            self.correct_answer = num1 + num2

        elif operation == '-':
            while num1 < num2:
                num1, num2 = random.randint(1, 100), random.randint(1, 100)
            self.correct_answer = num1 - num2

        elif operation == '*':
            while num1 * num2 > 100:
                num1, num2 = random.randint(1, 10), random.randint(1, 10)
            self.correct_answer = num1 * num2

        elif operation == '/':
            while num1 % num2 != 0 or num1 // num2 > 100:
                num1, num2 = random.randint(1, 100), random.randint(1, 10)
            self.correct_answer = num1 // num2

        self.current_question = f"{num1} {operation} {num2} = ?"
        self.problem_label.config(text=self.current_question)

    def check_answer(self, event):
        user_input = self.answer_input.get()
        if not user_input.isdigit():
            return

        user_answer = int(user_input)
        self.root.after(2000, lambda: self.evaluate_answer(user_answer))

    def evaluate_answer(self, user_answer):
        if user_answer == self.correct_answer:
            self.feedback_label.config(text="😄 გილოცავ", fg="green")
        else:
            self.feedback_label.config(text="😞 კიდევ სცადე", fg="red")

        self.root.after(2000, self.generate_question)

if __name__ == "__main__":
    root = tk.Tk()
    app = MathApp(root)
    root.mainloop()
