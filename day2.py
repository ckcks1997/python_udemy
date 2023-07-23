user_prom = "enter a todo:"


todos = []
while True:
    todo = input(user_prom)
    print(todo.capitalize()) # 글자 대문자
    print(todo.title()) #문장내 모든 단어의 첫 글자 대문자
    todos.append(todo)
    print(todos)
    print("and..")
