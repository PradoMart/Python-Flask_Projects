#TO DO LIST PROJECT

task_list = []
def add_task(task_list, task):
    task_list.append({"task_name": task, "status": False})
    print(f'Task created.')
    return

def see_tasks(task_list):
    print('---- TO DO LIST ----')
    for index, task in enumerate(task_list, start=1):
        check_status = '✓' if task["status"] else ' '
        print(f'{index}. [{check_status}] {task["task_name"]}')
    print('--------------------')



def update_task(task_list, task_index, new_task):
    correct_task_index = task_index - 1
    if correct_task_index >= 0 and correct_task_index < len(task_list):
        task_list[correct_task_index]["task_name"] = new_task
        print(f"Task updated!")
    else:
        print(f'Task not found!')
    
    return

def check_task(task_list, task_index):
    correct_task_index = task_index - 1
    if correct_task_index >= 0 and correct_task_index < len(task_list):
        task_list[correct_task_index]["status"] = True
        print(f"Task checked!")
    else:
        print(f'Task not found!')
    return

def delete_checked_taks(task_list):
    for task in task_list:
        if task["status"] == True:
            task_list.remove(task)
    print('Checked tasks was deleted.')
    return

while True:
    print("\n---- TO DO's TASK MENU ----")
    print("[1] - Add a Task")
    print("[2] - See your Tasks")
    print("[3] - Update a Task")
    print("[4] - Check a Task")
    print("[5] - Delete checked Tasks")
    print("[6] - Exit")
    print("----------------------------")

    choice = int(input("\nWhat is your choice? "))

    if choice == 6:
        print('\nThe program has finished. See you!\n')
        break
    
    elif choice == 1:
        task_name = str(input("\nWhat do you need TO DO? ")).strip().title()
        add_task(task_list,task_name)
        
    elif choice == 2:
        if len(task_list) == 0:
            print(f"You have NO task yet.")

        else:
            see_tasks(task_list)

    elif choice == 3:
        see_tasks(task_list)
        index = int(input("What task would you like to update? "))
        new_task = str(input("Write the new task: ")).strip().title()
        update_task(task_list, index, new_task)
    
    elif choice == 4:
        see_tasks(task_list)
        index = int(input("What task would you like to update? "))
        check_task(task_list, index)

    elif choice == 5:
        delete_checked_taks(task_list)
        see_tasks(task_list)