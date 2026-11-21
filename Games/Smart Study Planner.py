def welcome():
    print("\n---- Welcome to Smart Study Planner ----")

while True:
    welcome()

    name_subject = input("Enter name of subject: ")
    time = int(input(f"How many hours are needed for {name_subject}? "))
    free_days = input("Enter free days separated by a comma: ").split(", ")

    # إزالة المسافات الزائدة من أسماء الأيام
    free_days = [day.strip() for day in free_days]

    # توزيع الوقت بالتساوي
    study_time = time / len(free_days)

    print(f"\n📚 Study plan for '{name_subject}':")
    for day in free_days:
        print(f" - {day}: {study_time:.2f} Hour(s)")

    Exit = input("\nDo you want to leave? (Yes / No): ").strip().capitalize()
    if Exit == "Yes":
        break
