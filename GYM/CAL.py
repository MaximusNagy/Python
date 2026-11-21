def cal():
    print("\n--- Welcome to the Calorie Calculator! ---\n")
    print("1. Calculator with m and Kg")
    print("2. Calculator with cm and lb")
    print("3. Exit")


def Act():
    print("\nNow choose your Activity level")
    print("1.Sedentary (Little or no exercise)")
    print("2.Lightly Active (Exercise 1–3 days/week)")
    print("3.Moderately Active (Exercise 3–5 days/week)")
    print("4.Very Active (Exercise 6–7 days/week)")
    print("5.Extra Active (Very intense exercise or physical job)\n")


def get_number(prompt):
    # نفس فكرة input() بس بحماية من إدخال غلط
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


ACTIVITY_FACTORS = {
    "1": 1.2,
    "2": 1.375,
    "3": 1.55,
    "4": 1.725,
    "5": 1.9,
}


def calculate_tdee(bmr, weight_kg):
    # نفس منطق الاختيارات 1-5 بس بدل ما يتكرر 4 مرات، بقى مكان واحد
    Act()
    choice = input("Please,choice 1,2,3,4,5: ")
    factor = ACTIVITY_FACTORS.get(choice)
    if factor is None:
        print("please check your input ")
        return
    tdee = round(bmr * factor)
    print(f"Your The calories the body burns at rest is: {bmr}")
    print(f"Your Total Daily Energy Expenditure is: {tdee}")
    protein_grams = round(weight_kg * 1.8)
    fat_grams = round(weight_kg * 0.8)

    protein_calories = protein_grams * 4
    fat_calories = fat_grams * 9

    remaining_calories = tdee - protein_calories - fat_calories
    carb_grams = round(remaining_calories / 4)

    print("\n--- Your Macros ---")
    print(f"Calories: {tdee} kcal")
    print(f"Protein: {protein_grams} g")
    print(f"Carbs: {carb_grams} g")
    print(f"Fat: {fat_grams} g")


def calc_bmr(gender, age, height_cm, weight_kg):
    if gender in ("F", "f"):
        return round((10 * weight_kg) + (6.25 * height_cm) - (5 * age) - 161)
    else:
        return round((10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5)


def run_calculator(unit_choice):
    print("Please choose your Gender!")
    gender = input("F OR M: ")

    if gender in ("F", "f"):
        print("\nPlease enter your Height and age Weight\n")
        print("I know this secret for women but it's work\nI promise I won't tell this secret to anyone\n")

    if gender not in ("F", "f", "M", "m"):
        print("please check your input ")
        return

    age = get_number("Please enter your age: ")

    if unit_choice == "1":
        height_m = get_number("Please enter your height(m): ")
        weight_kg = get_number("Please enter your weight(kg): ")
        height_cm = height_m * 100
    else:  # unit_choice == "2"
        height_cm = get_number("Please enter your height(cm): ")
        weight_lb = get_number("Please enter your weight(lb): ")
        weight_kg = weight_lb * 0.453592

    bmr = calc_bmr(gender, age, height_cm, weight_kg)
    calculate_tdee(bmr, weight_kg)


loop = True
while loop:
    cal()
    choice_1 = input("Please,choice 1,2,3: ")
    if choice_1 == "3":
        print("Thanks for use Calorie Calculator")
        print("GOODBYE!")
        loop = False
    elif choice_1 in ("1", "2"):
        run_calculator(choice_1)
    else:
        print("please check your input ")