def work():
    print("\n--- Welcome to Workout Planner ---\n")
    print("1. Create your own plan")
    print("2. Let the app create your plan")
    print("3. Check your plan")
    print("4. Exit")


my_plan = {}

while True:
    work()
    choice = input("Please choose 1, 2, 3, or 4: ")

    if choice == "1":
        days = input(
            "What days do you exercise? Separate them with a comma: "
        ).split(",")

        for day in days:
            day = day.strip()

            exercises = input(
                f"What exercises do you do on {day}? Separate them with a comma: "
            ).split(",")

            my_plan[day] = [exercise.strip() for exercise in exercises]

    elif choice == "3":
        if not my_plan:
            print("Your plan is empty.")
        else:
            for day, exercises in my_plan.items():
                print(f"\n{day}:")
                for exercise in exercises:
                    print(f"- {exercise}")

    elif choice == "4":
        print("Goodbye!")
        break

    elif choice == "2":
        print("Automatic workout planning is not available yet.")

    else:
        print("Invalid choice.")