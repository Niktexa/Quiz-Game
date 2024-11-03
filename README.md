## Project Description
This is a True/False Quiz Game implemented in Python. 
It presents a series of questions to the player, who then answers each question as "True" or "False." 
The game tracks the player's score and displays feedback after each answer.

## Features
Randomized Questions: Questions are shuffled to provide a unique experience each time the game is played.
Score Tracking: The player's score is updated based on correct answers and displayed after each question.
Feedback: The game provides feedback on each answer, indicating if it was correct or incorrect.
Final Score: At the end of the game, the player’s total score is displayed.

## Project Structure
data.py: Contains question_data, a list of dictionaries with question text and answers.
question_model.py: Defines the Question class, which represents a question with its text and answer.
quiz_brain.py: Contains the QuizBrain class, which manages the question flow, score, and answer checking.
