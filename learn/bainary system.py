while True:
    print("\n*** Welcome to Number System Converter ***\n")
    print("1. Binary to Decimal")
    print("2. Decimal to Binary")
    print("3. Exit")
    
    choose = input("Enter your choice: ")

    if choose == "1":
        binary_val = input("Enter a binary number: ")
        # تحويل من ثنائي لعشري
        decimal_val = int(binary_val, 2)
        print(f"Decimal Result: {decimal_val}")

    elif choose == "2":
        decimal_input = input("Enter a decimal number: ")
        # بنحوله لـ int الأول عشان دالة bin بتتعامل مع أرقام مش نصوص
        decimal_num = int(decimal_input) 
        # دالة bin بتطلع النتيجة بتبدأ بـ 0b، فبنستخدم [2:] عشان نشيلهم
        binary_val = bin(decimal_num)[2:]
        print(f"Binary Result: {binary_val}")

    elif choose == "3":
        print("Exiting... Goodbye!")
        break
    
    else:
        print("Invalid choice, please try again.")