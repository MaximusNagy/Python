list_yes = []
list_no = []

# إدخال المهام مع تنظيف المسافات الزائدة
to_do = input("Enter your tasks for today separated by a comma: ").split(", ")
to_do = [task.strip() for task in to_do]

for task in to_do:
    print(f"\n{task}\n")
    
    task_do = input(f"Did you finish {task} already? (yes/no): ").lower()

    if task_do == "yes":
        list_yes.append(task)
        print("\nNice job!")
    else:
        list_no.append(task)
        print("\nTry not to put it off.")
    print("-----")

do = input("\nDo you want to see your today's progress? (yes/no): ").lower()
if do == "yes":
    print("\n**** Done Tasks ****")
    print(list_yes if list_yes else "No tasks completed yet.")
    
    print("\n**** Ongoing Tasks ****")
    print(list_no if list_no else "All tasks are done!")
else:
    input( "Plese hit Enter to exit")

print("\nHave a great productive day!")