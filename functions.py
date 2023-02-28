def get_todos():
    with open('todo.txt', 'r') as f:
        return f.readlines()


def add_todos(todos):
    with open('todo.txt', 'w') as f:
        for todo in todos:
                f.writelines(todo)
