user_prompt= "type add or show\n"
todos=[]
while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    if 'add' in user_action:
        todo = user_action[4:]

        with open("files/todos.txt", 'r') as file:
            todos = file.readlines()

        todos.append(todo)
        with open("files/todos.txt", 'w') as file:
            file.writelines(todos)

    elif ('show' or 'display') in user_action:
        with open("files/todos.txt", 'r') as file:
            todos = file.readlines()

        # new_todos=[]
        # for item in todos:
        #     new_item = item.strip('\n')
        #     new_todos.append(new_item)
        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            row = f"{index+1}-{item}"
            print(row, end='')

    elif 'edit' in user_action:
        number = int(input('enter num:'))
        number = number - 1

        with open("files/todos.txt", 'r') as file:
            todos = file.readlines()
        print('here is todos existing', todos)

        new_todo = input('enter new todo:')
        todos[number] = new_todo + '\n'

        with open("files/todos.txt", 'w') as file:
            file.writelines(todos)

    elif 'complete' in user_action:
        number = int(input("number of the todo list to complete: \n"))
        index = number -1
        todo_to_remove = todos[index].strip('\n')

        with open("files/todos.txt", 'r') as file:
            todos = file.readlines()

        todos.pop(index)

        with open("files/todos.txt", 'w') as file:
            file.writelines(todos)

        message = f'Todo: {todo_to_remove} removed'
        print(message)

    elif 'exit' in user_action:
        break
    else:
        print("try again: ")

# mutable, immutable
#list is mutable
filenames = ['1.txt', '2.txt', '3.txt']
#tuple is not.
sometuple = ("1", "2", "3")


