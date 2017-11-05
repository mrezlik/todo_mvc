import todo_item


class TodoItem():

    def __init__(self):
        self.todo_items = []

    def add_item(self, name, description):
        self.todo_items.append(todo_item.Task(name, description))

    def mark_as_done(self, index):
        self.todo_items[index-1].is_done = True

    def delete_task(self, index):
        self.todo_items.pop(index-1)

    def display_tasks(self):
        for i in range(len(self.todo_items)):
            print("TASK {0}\n\tID: {0}\n\tName: {1}".format(i+1, self.todo_items[i].name))

    def display_information_about_task(self, index):
        return("ID: {0}\n Name: {1}\n Description: {2}\n Is done: {3}".format(index, self.todo_items[index-1].name, self.todo_items[index-1].description, self.todo_items[index-1].is_done))

    def modifify_task(self, index, new_name, new_description):
        self.todo_items[index-1].name = new_name
        self.todo_items[index-1].description = new_description
