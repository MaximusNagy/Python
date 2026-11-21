import math

def cal():
    print("\n--- Welcome ---")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Sine (sin)")
    print("6. Cosine (cos)")
    print("7. Tangent (tan)")
    print("8. Power (x^y)")
    print("9. Exit")

while True:
    cal()
    choose = input("Choose [1-9]: ")

    if choose in {"1", "2", "3", "4", "8"}:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choose == "1":
                print("Result:", num1 + num2)
            elif choose == "2":
                print("Result:", num1 - num2)
            elif choose == "3":
                print("Result:", num1 * num2)
            elif choose == "4":
                if num2 != 0:
                    print("Result:", num1 / num2)
                else:
                    print("Error: Division by zero.")
            elif choose == "8":
                print("Result:", num1 ** num2)
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    elif choose in {"5", "6", "7"}:
        try:
            angle = float(input("Enter the angle in degrees: "))
            radians = math.radians(angle)

            if choose == "5":
                print("Result:", math.sin(radians))
            elif choose == "6":
                print("Result:", math.cos(radians))
            elif choose == "7":
                print("Result:", math.tan(radians))
        except ValueError:
            print("Invalid input. Please enter a valid angle.")

    elif choose == "9":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select between 1 and 9.")
