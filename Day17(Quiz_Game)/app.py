from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create a list of Question objects from the data
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

# Initialize quiz engine
quiz  = QuizBrain(question_bank)

# Run quiz loop while questions remain
while quiz.still_has_questions():
    quiz.next_question()

# Final results
print("You've completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")