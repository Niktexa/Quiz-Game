from data import question_data

class Question:
    def __init__ (self, text, b_answer):
        self.text = text
        self.answer = b_answer

    def __repr__(self):
        return f"{self.text}: {self.answer}"

