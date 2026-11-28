def choose():
    print("\n--- Welocome to Gym Tracer ---\n")
    print("1.Bmi Calculator")
    print("2.calorie calculator")
    print("3.Workouts")
    print("4.Exit")
choose()
core= True
while core:
    choice = input("Please choose 1,2,3,4: ")
    if choice=="1":
        from bmi_calculator import main
    elif choice=="2":
        import calorie_calculator
    elif choice=="3":
        pass
    elif choice=="4":
        print("Thanks for use Gym Tracker")
        print("GOODBYE!")
        core=False
    else:
        print("Please check your input.")
