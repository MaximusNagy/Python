import math
def show_units():
    print("\n--- Welcome to the Calorie Calculator! ---\n")
    print("1. Calculator with m and Kg")
    print("2. Calculator with cm and lb")
    print("3. Exit")

def show_activity_menu():
    print("\nNow choose your Activity level")
    print("1.Sedentary (Little or no exercise)")
    print("2.Lightly Active (Exercise 1–3 days/week)")
    print("3.Moderately Active (Exercise 3–5 days/week)")
    print("4.Very Active (Exercise 6–7 days/week)")
    print("5.Extra Active (Very intense exercise or physical job)\n")
    while True:
        activity = input("Choose your activity in (1-5):")

        if activity not in ["1", "2", "3", "4", "5"]:
            print("Invalid input!")
            continue

        return activity

ACTIVITY_FACTORS = {
    "1": 1.2,
    "2": 1.375,
    "3": 1.55,
    "4": 1.725,
    "5": 1.9,
}

def get_user_data():
    while True:
        show_units()
        try:
            choice = input("Enter your choice:")

            if choice == "1":
                weight = float(input("Enter your weight Kilogram (kg): "))
                if weight <= 0:
                    print("Weight must be greater than zero")
                    continue
                height_m = float(input("Enter your height Meter (m): "))
                if height_m <= 0:
                    print("Height must be greater than zero")
                    continue
                height = height_m * 100
            elif choice == "2":
                weight_lb = float(input("Enter your weight in Pound (lb): "))
                height = float(input("Enter your height Centimeter (cm): "))
                if weight_lb <= 0 or height <= 0:
                    print("Weight and height must be greater than zero")
                    continue
                weight = weight_lb * 0.45359237
            elif choice == "3":
                print("Good bye! 👋🏼")
                return None

            else:
                print("Invalid choice!")
                continue

            age = int(input("Enter your age: "))

            if age <= 0 or age > 120:
                print("Age must be between 1 and 120")
                continue 
        except ValueError:
                print("Invalid input! Please enter numeric values only.")  
                continue
        while True:
            gender = input("choose your gender in (Male, Female): ").capitalize()
            if gender not in ["Male", "Female"]:
                print("Enter your gender correct!")
                continue
            return (age, weight, height, gender)
        
def calculate_bmr(age, weight, height, gender):
    if gender == "Male":
        bmr= 10 * weight + 6.25* height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    return bmr

def calculate_tdee(bmr, activity):
    factor = ACTIVITY_FACTORS.get(activity)
    if factor is None:
        return None
    tdee = bmr * factor
    return tdee

def show_goal_menu(tdee):  
    print("\n--- Choose Your Goal ---")
    print("1. Lose Weight")
    print("2. Maintain Weight")
    print("3. Gain Weight")
    while True:
        goal = input("Choose your goal (1-3): ")
        if goal == "1":
            target_calories = tdee - 500
        elif goal == "2":
            target_calories = tdee
        elif goal == "3":
            target_calories = tdee + 500
        else:
            print("Invalid choose!")
            continue
        return target_calories

def calculate_macros(target_calories):
    print("1. You want to choose macro ratios")
    print("2. Or let the application choose the natural one")
    while True:
        choose = input("Enter your choice (1-2): ")
        if choose == "1":
            while True:
                try:
                    pct_protein = float(input("Enter the percentage of protein: "))/100
                    pct_carbs   = float(input("Enter the percentage of carbs: ")) /100
                    pct_fats    = float(input("Enter the percentage of fats: ")) /100
                    if not all(0 <= p <= 1 for p in [pct_protein, pct_carbs, pct_fats]):
                        print("Each percentage must be between 0 and 100!")
                        continue
                    elif not math.isclose(pct_protein + pct_carbs + pct_fats, 1.0):
                        print("The total percentages must equal 100!")
                        continue
                    protein = round((target_calories * pct_protein) / 4)
                    carbs = round((target_calories * pct_carbs) / 4)
                    fats = round((target_calories * pct_fats) / 9)
                except ValueError:
                    print("Invalid input! Please enter numeric values only.")  
                    continue
                break
        elif choose == "2":
            protein = round((target_calories * 0.30) / 4)
            carbs = round((target_calories * 0.40) / 4)
            fats = round((target_calories * 0.30) / 9)

        else:
            print("Invalid choice!")
            continue
        return protein, carbs, fats

def show_result(target_calories, protein, carbs, fats):
    print(f"\nYour daily calories: {target_calories:.1f}")
    print(f"Your macros:")
    print(f"Protein: {protein:.1f} g")
    print(f"Carbs: {carbs:.1f} g"    )
    print(f"Fats: {fats:.1f} g"      )

def main():
    user_data= get_user_data()
    if user_data is None:
        return
    age, weight, height, gender = user_data
    
    activity= show_activity_menu()
    bmr = calculate_bmr(age, weight, height, gender)
    tdee = calculate_tdee(bmr, activity)
    target_calories = show_goal_menu(tdee)
    protein, carbs, fats = calculate_macros(target_calories)
    show_result(target_calories, protein, carbs, fats)
if __name__ == "__main__":
    main()
