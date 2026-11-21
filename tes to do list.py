def to_do():
    print("\n**** Welcome to To do list ****")
    print("1. Enter the task")
    print("2. Show tasks")
    print("3. Delete task")
    print("4. Edite task")
    print("5. Exit")

tasks =[]
# length= 1
while True:
    to_do()
    num_function = input("\nEnter the number: ")
    if num_function =="1":
        task = input("Enter the task: ")
        tasks.append(task)
    elif num_function =="2":
        if tasks:
            for i in range(1,len(tasks)+1):
                print(f"{i}: {tasks[i - 1]}")

                # length +=1
        else:
            print("Don't have task for show!")
    elif num_function =="3":
        if tasks:
            for i in range(1,len(tasks)+1):
                print(f"{i}: {tasks[i - 1]}")
            num_remove = int(input("Enter the number task for remove: "))
            task_remove=tasks.pop(num_remove-1)
            print(f"Sucssfully! removed task : {task_remove}")
    elif num_function =="4":
        if tasks:
            for i in range(1,len(tasks)+1):
                print(f"{i}: {tasks[i - 1]}")
            num_edite = int(input("Enter the number task for edite: "))
            if num_edite > len(tasks)+1 or num_edite < len(tasks) +1:
                num_edite = int(input("Enter the number task for edite: "))
            new_edite =(input("Enter the name task for add: "))
            old_task = tasks[num_edite - 1]
            tasks[num_edite - 1] = new_edite
            print(f"Task updated successfully!: from {old_task}: to {new_edite}")
        else:
            print("Don't have task for Edite!")
    else:
        print("Good Bye!")
        break
    
