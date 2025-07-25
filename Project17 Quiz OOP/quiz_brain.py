import html
class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        current_question_text = html.unescape(current_question.text)
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question_text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        # print(f"You guessed {user_answer}, the correct answer was {correct_answer}")
        # print(f"So...{correct_answer == user_answer}")
        if user_answer.lower() == correct_answer.lower():
            print("Well done!")
            self.score += 1
        else:
            print("Not right!")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}\n")

    def quiz_over(self):
        print(f"You completed the quiz")
        print(f"Your final score was: {self.score}/{self.question_number}")