import todo_item


class TodoItem():

    def __init__(self):
        self.todo_items = []

    def add_item(self):
        name_length = 21
        description_length = 151
        while name_length > 20:
            name = input("Please enter a name of task (max 20 characters)")
            name_length = len(name)
        while description_length > 150:
            description = input("Please enter a description of task (max 150 characters)")
            description_length = len(description)
        self.todo_items.append(todo_item.Task(name, description))
