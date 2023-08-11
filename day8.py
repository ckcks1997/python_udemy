user_prompt= "type add or show\n"
todos=[]
while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("enter todo\n") + "\n"
            #with문을 사용하면 file을 close 하지 않아도 된다.
            with open("files/todos.txt", 'r') as file:
                todos = file.readlines()

            todos.append(todo)
            with open("files/todos.txt", 'w') as file:
                file.writelines(todos)

        case 'show' | 'display':
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

        case 'edit':
            number = int(input('enter num:'))
            number = number - 1

            with open("files/todos.txt", 'r') as file:
                todos = file.readlines()
            print('here is todos existing', todos)

            new_todo = input('enter new todo:')
            todos[number] = new_todo + '\n'

            with open("files/todos.txt", 'w') as file:
                file.writelines(todos)

        case 'complete':
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

        case 'exit':
            break
        case ann:
            print("ann is annonymous value, and it's default case!\n usually, we use _ instead of ann")

# mutable, immutable
#list is mutable
filenames = ['1.txt', '2.txt', '3.txt']
#tuple is not.
sometuple = ("1", "2", "3")


