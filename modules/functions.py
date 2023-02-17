FILEPATH = "todos.txt"


def get_todos(filepath = FILEPATH):
    """Read a text file and return a list of
    To Do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath = FILEPATH):
    """Write a To Do python list in the a text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == '__main__':
    print('hello')