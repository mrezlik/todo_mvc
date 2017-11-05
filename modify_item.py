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

    def mark_as_done(self, index):
        self.todo_items[index-1].is_done = True

    def delete_task(self, index):
        self.todo_items.pop(index-1)

    def display_tasks(self):
        if len(self.todo_items) == 0:
            return "You don't add any task!"
        else:
            for i in range(len(self.todo_items)):
                print("ID: {0}\n Name: {1}".format(i+1, self.todo_items[0].name))

    def display_information_about_task(self, index):
        print("ID: {0}\n Name: {1}\n Description: {2}\n Is done: {3}".format(index, self.todo_items[index-1].name, self.todo_items[index-1].description, self.todo_items[index-1].is_done))

    def modifify_task(self, index):
        self.todo_items[index-1].name = input("Please enter a new name of task:")
        self.todo_items[index-1].description = input("Please enter a new desciprion of task")
