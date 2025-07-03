from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []

for q_and_a in question_data:
    question_bank.append(
        Question(q_and_a["question"], q_and_a["correct_answer"])
    )

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("Goodbye")

quiz.quiz_over()