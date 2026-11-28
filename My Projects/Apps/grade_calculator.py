print("\n**** Welcome to Grade Calculator ****")

num_subjects = int(input("Enter the number of subjects: "))
total_score = 0
total_max = 0

for num in range(1, num_subjects + 1):
    score = float(input(f"Enter your score for subject #{num}: "))
    max_score = float(input(f"What is the total score for subject #{num}?: "))
    total_score += score
    total_max += max_score

percentage = (total_score / total_max) * 100

print(f"\nYour total percentage is: {percentage:.2f}%")

if percentage >= 90:
    print("Your grade is: Excellent 😎😎")
elif percentage >= 80:
    print("Your grade is: Very Good 😎")
elif percentage >= 70:
    print("Your grade is: Good 🙂")
elif percentage >= 60:
    print("Your grade is: Passable 😐")
else:
    print("Your grade is: Poor 😢")
