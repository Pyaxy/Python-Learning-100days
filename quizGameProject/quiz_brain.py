

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(
            f"Q."
            f"{self.question_number + 1} "
            f"{current_question.text}"
            f" (True/False)")
        self.question_number += 1
        self.check_answer(user_answer, current_question.answer)

    def still_have_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, current_answer):
        if user_answer.lower() == current_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")
        print(f"The correct answer is {current_answer}!")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
