user_prompt= "type add or show\n"
todos=[]
while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("enter todo\n") + "\n"
            file = open("files/todos.txt", 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)
            file = open('files/todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show' | 'display':
            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            # new_todos=[]
            # for item in todos:
            #     new_item = item.strip('\n')
            #     new_todos.append(new_item)
            new_todos = [item.strip('\n') for item in todos]
            print(todos)
            print(new_todos)

            for index, item in enumerate(todos):
                row = f"{index}-{item}"
                print(row, end='')

        case 'edit':
            number = int(input('enter num:'))
            if(number <= len(todos)):
                str = input('enter str:')
                todos[number-1] = str
        case 'complete':
            number = int(input("number of the todo list to complete"))
            todos.pop(number)
        case 'exit':
            break
        case ann:
            print("ann is annonymous value, and it's default case!\n usually, we use _ instead of ann")

# mutable, immutable
#list is mutable
filenames = ['1.txt', '2.txt', '3.txt']
#tuple is not.
sometuple = ("1", "2", "3")


