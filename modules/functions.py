def get_todos(filepath="files/todos.txt"):
    """ Read a text file and return the list of to-do items."""
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos_arg, filepath="files/todos.txt"):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("hello")