def get_todos():
    with open("files/todos.txt", 'r') as file:
        todos = file.readlines()
    return todos


user_prompt = "type add or show\n"
todos = []
while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        with open("files/todos.txt", 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('show'):
        todos = get_todos()

        # new_todos=[]
        # for item in todos:
        #     new_item = item.strip('\n')
        #     new_todos.append(new_item)
        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            row = f"{index + 1}-{item}"
            print(row, end='')

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = get_todos()

            new_todo = input('enter new todo:')
            todos[number] = new_todo + '\n'

            with open("files/todos.txt", 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid. try again ")
            continue  # continue를 할 경우 아래 코드들은 무시됨

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open("files/todos.txt", 'w') as file:
                file.writelines(todos)

            message = f'Todo: {todo_to_remove} removed'
            print(message)

        except IndexError:
            print("there is no item with that err")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("try again: ")

# mutable, immutable
# list is mutable
filenames = ['1.txt', '2.txt', '3.txt']
# tuple is not.
sometuple = ("1", "2", "3")
