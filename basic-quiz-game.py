import tkinter as tk
from tkinter import messagebox

# Questions, options, and correct answers
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["New Delhi", "Mumbai", "Chennai", "Kolkata"],
        "answer": "New Delhi"
    },
    {
        "question": "Which river is known as the 'Ganga of the South'?",
        "options": ["Krishna", "Kaveri", "Godavari", "Narmada"],
        "answer": "Kaveri"
    },
    {
        "question": "Who was the first Prime Minister of India?",
        "options": ["Mahatma Gandhi", "Jawaharlal Nehru", "Indira Gandhi", "Sardar Patel"],
        "answer": "Jawaharlal Nehru"
    },
    {
        "question": "Which is the national animal of India?",
        "options": ["Lion", "Elephant", "Tiger", "Peacock"],
        "answer": "Tiger"
    },
    {
        "question": "What is the national flower of India?",
        "options": ["Rose", "Lily", "Lotus", "Marigold"],
        "answer": "Lotus"
    },
    {
        "question": "Which is the largest state in India by area?",
        "options": ["Uttar Pradesh", "Maharashtra", "Rajasthan", "Madhya Pradesh"],
        "answer": "Rajasthan"
    },
    {
        "question": "In which year did India gain independence?",
        "options": ["1945", "1946", "1947", "1948"],
        "answer": "1947"
    },
    {
        "question": "Who is known as the 'Father of the Nation' in India?",
        "options": ["Subhas Chandra Bose", "Mahatma Gandhi", "Bhagat Singh", "Jawaharlal Nehru"],
        "answer": "Mahatma Gandhi"
    },
    {
        "question": "Which festival is known as the 'Festival of Lights'?",
        "options": ["Holi", "Diwali", "Eid", "Christmas"],
        "answer": "Diwali"
    },
    {
        "question": "What is the national bird of India?",
        "options": ["Sparrow", "Eagle", "Peacock", "Parrot"],
        "answer": "Peacock"
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.score = 0
        self.current_question = 0

        self.question_label = tk.Label(root, text="", wraplength=400, justify="center", font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.buttons = []
        for i in range(4):
            button = tk.Button(root, text="", width=50, font=("Arial", 12), command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.buttons.append(button)

        self.feedback_label = tk.Label(root, text="", font=("Arial", 12))
        self.feedback_label.pack(pady=20)

        self.next_button = tk.Button(root, text="Next", command=self.next_question, state=tk.DISABLED)
        self.next_button.pack(pady=20)

        self.show_question()

    def show_question(self):
        question_data = questions[self.current_question]
        self.question_label.config(text=question_data["question"])
        for i, option in enumerate(question_data["options"]):
            self.buttons[i].config(text=option, state=tk.NORMAL)
        self.feedback_label.config(text="")
        self.next_button.config(state=tk.DISABLED)

    def check_answer(self, index):
        question_data = questions[self.current_question]
        selected_option = question_data["options"][index]
        if selected_option == question_data["answer"]:
            self.feedback_label.config(text="Correct!", fg="green")
            self.score += 1
        else:
            self.feedback_label.config(text=f"Wrong! The correct answer was {question_data['answer']}.", fg="red")

        for button in self.buttons:
            button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(questions):
            self.show_question()
        else:
            messagebox.showinfo("Quiz Completed", f"Your final score is {self.score}/{len(questions)}.")
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
