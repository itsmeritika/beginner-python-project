def task():
    tasks = [] # empty list
    print("Welcome to the task management app")
    total_task = int(input("Enter how many task you want to add = "))
    for i in range(1, total_task+1):
        task_name= input(f"Enter task {i} = ")
        tasks.append(task_name)
    print(f"Today's tasks are\n {tasks}")
    while True:
        operation = int(input("Enter 1-Add\n 2-update\n 3-Delete\n 4-view\n 5-Exit/stop/"))
        if operation == 1:
            add = input("Enter task you want to add=")
            tasks.append(add)
            print(f"Task {add} has been added successfully")
        elif operation==2 :
            update_val = input("Enter the task name you want to update=")
            if update_val in tasks:
                up = input("Enter new task = ")
                ind =  tasks.index(update_val)
                tasks[ind] = up    
                print(f"updated task {up}") 
        elif operation==3:
            del_val = input("which task you want to delete = ")
            if del_val in tasks:
                ind = tasks.ind(del_val)
                del tasks[ind]
                print(f"Task {del_val} has been deleted")
        elif operation == 4:
            print(f"Total tasks = {tasks}")
        elif operation == 5:
            print("closing the program")
            break
        else:
            print("Wrong choice")
task()



  
