from question_model import Question
from data import question_data
from quiz_brain import QuizeBrain

question_bank = []
for data in question_data:
  question_text = data["text"]
  question_answer = data["answer"]
  new_question = Question(question_text, question_answer)
  question_bank.append(new_question)


quiz = QuizeBrain(question_bank)

while quiz.still_has_questions():
  quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score is {quiz.score}/{quiz.question_number}.")