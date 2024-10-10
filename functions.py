FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Read the text file and return every line as an item inside a list object.
    :param filepath: File to read
    :return: List of to-dos
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Write or overwrite the text file in the path, creating a line for each
    element of the list.
    :param todos_arg: List of to-dos
    :param filepath: File to write/overwrite
    :return: None
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print(get_todos())
