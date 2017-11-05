import os
from modify_item import TodoItem


def menu():
    DEFAULT_NAME_MAX_LENGTH = 21
    DEFAULT_DESCIPRTION_MAX_LENGTH = 151
    td = TodoItem()
    is_end = False
    print("Hello! This is my ToDo app! What do you want to do?")
    while is_end == False:
        print("\t\t1. Add task \n \
               2. Remove task \n \
               3. Modify task \n \
               4. Mark task as done \n \
               5. Display all tasks \n \
               6. Display information about task \n \
               7. Exit")
        while True:
            try:
                user_input = int(input("Which option you choose?"))
            except ValueError:
                print("Please enter number from 1 to 7!")
            else:
                break
        if user_input == 7:
            exit()
        elif user_input == 1:
            while True:
                name = input("Please enter name of task (max 20 characters)")
                if len(name) < DEFAULT_NAME_MAX_LENGTH:
                    pass
                else:
                    print("You task name is too long!")
                description = input("Please enter descirption of task (max 50 characters)")
                if len(description) < DEFAULT_DESCIPRTION_MAX_LENGTH:
                    td.add_item(name, description)
                    break
                else:
                    print("You task descirption is too long!")
        elif user_input == 2:
            while True:
                user_input_is_int = False
                while user_input_is_int == False:
                    try:
                        choosen_task= int(input("Which task do you want to remove?(to back enter 0): "))
                    except ValueError:
                        print("Please enter a number!")
                    else:
                        user_input_is_int = True
                if choosen_task == 0:
                    break
                try:
                    td.delete_task(choosen_task)
                except IndexError:
                    print("You can't remove task which doesn't exist!")
                else:
                    print("You remove task!")
                    break
        elif user_input == 3:
            user_input_is_int = False
            while user_input_is_int == False:
                try:
                    choosen_task = int(input("Which task do you want to modify?(to back enter 0): "))
                except ValueError:
                    print("Please enter a number!")
                else:
                    if choosen_task > len(td.todo_items):
                        print("You can't modify task which doesn't exist!")
                    else:
                        user_input_is_int = True
            if choosen_task == 0:
                break
            while True:
                new_name = input("Please enter new name of task (max 20 characters)")
                if len(new_name) < DEFAULT_NAME_MAX_LENGTH:
                    pass
                else:
                    print("You task name is too long!")
                new_description = input("Please enter new descirption of task (max 50 characters)")
                if len(new_description) < DEFAULT_DESCIPRTION_MAX_LENGTH:
                    td.modifify_task(choosen_task, new_name, new_description)
                    break
                else:
                    print("You task descirption is too long!")
        elif user_input == 4:
            user_input_is_int = False
            while user_input_is_int == False:
                try:
                    choosen_task = int(input("Which task do you want to mark as done?(to back enter 0): "))
                except ValueError:
                    print("Please enter a number!")
                else:
                    if choosen_task > len(td.todo_items):
                        print("You can't mark task which doesn't exist!")
                    else:
                        user_input_is_int = True
            if choosen_task == 0:
                break
            td.mark_as_done(choosen_task)
            print("You mark task as done!")
        elif user_input == 5:
            td.display_tasks()
            input("Press enter to back!")
        elif user_input == 6:
            user_input_is_int = False
            while user_input_is_int == False:
                try:
                    choosen_task = int(input("Which task do you want to show?(to back enter 0): "))
                except ValueError:
                    print("Please enter a number!")
                else:
                    if choosen_task > len(td.todo_items):
                        print("You can't show task which doesn't exist!")
                    else:
                        user_input_is_int = True
            if choosen_task == 0:
                break
            print(td.display_information_about_task(choosen_task))
            input("Please enter to back!")


def main():
    menu()


if __name__ == "__main__":
    main()
