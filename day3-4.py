user_prompt= "type add or show\n"
todos=[]
while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo=input("enter todo\n")
            todos.append(todo)
        case 'show' | 'display':
            for item in todos:
                print(item)
        case 'edit':
            number = int(input('enter num:'))
            if(number <= len(todos)):
                str = input('enter str:')
                todos[number-1] = str
        case 'exit':
            break
        case ann:
            print("ann is annonymous value, and it's default case!\n usually, we use _ instead of ann")

# mutable, immutable
#list is mutable
filenames = ['1.txt', '2.txt', '3.txt']
#tuple is not.
sometuple = ("1", "2", "3")


