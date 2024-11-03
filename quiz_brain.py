from data import question_data

class QuizBrain():
    
    def __init__(self, question_list):
        self.question_num = 0
        self.question_list = question_list
        self.score = 0
        

    def next_q(self):
        first_q = self.question_list[self.question_num]
        user_answer = input(f"{self.question_num+1}. {first_q.text} True/False: ")
        self.answer_check(user_answer, first_q)
        self.question_num += 1
        print(f"Score: {self.score}/{len(self.question_list)}")
    

    def another_q(self):
        return self.question_num < len(self.question_list)
            
        
    def answer_check(self, user_answer, first_q):
        if user_answer.lower() == first_q.answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect!")

    