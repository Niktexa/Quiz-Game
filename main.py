from data import question_data
from question_model import Question
import random
from quiz_brain import QuizBrain


random.shuffle(question_data)

question_bank = [Question(item['text'], item['answer']) for item in question_data]

q_can = QuizBrain(question_bank)

while q_can.another_q():
    q_can.next_q()


