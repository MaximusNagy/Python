def BMI():
    def cal():
        print("\n--- Welcome to BMI Calculator ---")
        print("1. Calculator with m")
        print("2. Calculator with cm")
        print("3. Exit")

    while True:
        cal()
        cal_choice = input("Enter your choice: ")

        if cal_choice == "3":
            print("Goodbye!")
            break

        elif cal_choice in ["1", "2"]:
            try:


                if cal_choice == "1":
                    height = float(input("Enter your height (in meters): "))
                    weight = float(input("Enter your weight (kg): "))
                    if height <= 0:
                        print("Height must be greater than zero.")
                        continue
                    result = weight / (height ** 2)

                elif cal_choice == "2":
                    height_cm = float(input("Enter your height (in cm): "))
                    weight = float(input("Enter your weight (kg): "))
                    if height_cm <= 0:
                        print("Height must be greater than zero.")
                        continue
                    height_m = height_cm / 100
                    result = weight / (height_m ** 2)

                print(f"Your BMI is: {result:.2f}")

                if result < 18.5:
                    print("You are underweight.")
                elif 18.5 <= result < 25:
                    print("You have a normal weight.")
                elif 25 <= result < 30:
                    print("You are overweight.")
                elif 30 <= result < 35:
                    print("You are obese (Class 1).")
                elif 35 <= result < 40:
                    print("You are obese (Class 2).")
                else:
                    print("You are severely obese (Class 3).")

            except ValueError:
                print("Invalid input! Please enter numeric values only.")
        else:
            print("Invalid choice, please enter 1, 2, or 3.")

BMI()
        
    # weight = int(input("Enter your weight: "))
    # height = float(input("Enter your height (in meters): "))
    # height_squared = height * height
    # result = weight / height_squared