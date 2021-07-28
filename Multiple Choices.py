question_prompts = [
    "What is an apple?\nVeggie\nFruit\n\n",
    "\nYou are a?\nHuman\nAnimal\n\n",
    "\nIs a bread delicious?\nYes\nNo\n\n"
]

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questions = [
    Question(question_prompts[0], "Fruit"),
    Question(question_prompts[1], "Human"),
    Question(question_prompts[2], "Yes"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("\nYour score: " + str(score) + "/" + str(len(questions)))

run_test(questions)
