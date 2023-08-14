import json
with open("questions.json", "r") as file:
    content = file.read()

data = json.loads(content)
print(data)
score=0

for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index+1,'-' ,alternative)

    user_choice = int(input("enter your answer: "))
    question['user_choice'] = user_choice
    if question['correct_answer'] ==  question['user_choice']:
        print("correct")
        score += 1
        print("score:", score)
    else:
        print("wrong")
        print("score:", score)


for index, question in enumerate(data):
    message = (f"{index + 1} - your answer: {question['user_choice']}, "
               f"Correct answer: {question['correct_answer']}")
    print(message)