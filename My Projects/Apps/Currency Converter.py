def cal():
    print("\n--- Currency conversion ---")
    print("1. From EGP to USD")
    print("2. From AED to EGP")  # تصحيح الخطأ الإملائي (ot → to)
    print("3. Exit")

USD_RATE = 50.59  # 1 USD = 50.59 EGP (سعر صرف افتراضي)
AED_RATE = 13.77  # 1 AED = 13.77 EGP (سعر صرف افتراضي)

while True:
    cal()
    choose = input("Enter your choice: ")

    if choose == "3":
        print("Thanks for using the app, GOOD BYE!")
        break
    elif choose == "1":
        try:
            amount = float(input("Enter the amount in EGP: "))  # توضيح العملة
            result = amount / USD_RATE
            print(f"Result: {amount} EGP = {result:.2f} USD")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
    elif choose == "2":
        try:
            amount = float(input("Enter the amount in AED: "))  # توضيح العملة
            result = amount * AED_RATE
            print(f"Result: {amount} AED = {result:.2f} EGP")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
    else:
        print("Invalid option. Please choose 1, 2, or 3.")