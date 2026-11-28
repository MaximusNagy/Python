def show_menu():
        print("\n--- Welcome to BMI Calculator ---\n")
        print("1. Calculator with m")
        print("2. Calculator with cm")
        print("3. Exit")

def get_height():
    while True:    
        show_menu()
        choice =input("Enter your choice: ")
        if choice == "3":
            print("Good bye 🙋🏼‍♂️")
            return None
        try:
            if choice =="1":
                height = float(input("Enter your height in meter: "))
                if height <= 0 :
                    print("Height must be greater than zero")
                    continue
            elif choice =="2": 
                height_cm = float(input("Enter your height in centimeter: "))
                height = height_cm / 100
                if height_cm <= 0 :
                    print("Height must be greater than zero")
                    continue
            else:
                print("Invalid choice")
                continue
        except ValueError:
                print("Invalid input! Please enter numeric values only.")
                continue


        return height

def get_weight():
    while True:
        try:
            weight = float(input("Enter your weight in Kilograms: "))
            if weight <= 0:
                print("Weight must be greater than zero")
                continue
        except ValueError:
                print("Invalid input! Please enter numeric values only.")  
                continue
        return weight

def calculate_bmi(height, weight):
    bmi = (weight / (height**2))
    return bmi

def show_result(bmi):
    print(f"Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
        print("You are underweight.")
    elif bmi < 25:
        print("You have a normal weight.")
    elif bmi < 30:
        print("You are overweight.")
    elif bmi < 35:
        print("You are obese (Class 1).")
    elif bmi < 40:
        print("You are obese (Class 2).")
    else:
        print("You are severely obese (Class 3).")

def main():
    while True:
        height = get_height()
        if height is None:
            break
        weight = get_weight()
        bmi = calculate_bmi(height, weight)
        show_result(bmi)

main()
