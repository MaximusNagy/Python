def cal():
    while True:
        print("\n--- PET_CONVERSION ---")
        print("1. Convert Normal to Golden Pets and (Check Calculation for legendary)")
        print("2. Convert Golden to Rainbow Pets and (Check Calculation for legendary)")
        print("3. Convert Rainbow to Void Pets and (Check Calculation for legendary)")
        print("4. Exit")

        choice = input("Enter your choice: ")

        # Define conversion and cost rates to avoid repetition
        conversion_rates = {
            "golden": 5,
            "rainbow": 5 * 5,  # equals 25
            "void": 5 * 5 * 5  # equals 125
        }
        cost_rates = {
            "golden": 150,
            "rainbow": 300,
            "void": 120000
        }

        if choice in ["1", "2", "3"]:
            try:
                many_pet = int(input("Enter the number of pets: "))
                if many_pet < 1:
                    print("Please enter a valid number greater than 0.")
                    continue
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                continue

            # Determine pet type based on user's choice
            if choice == "1":
                pet_type = "golden"
            elif choice == "2":
                pet_type = "rainbow"
            else:  # choice == "3"
                pet_type = "void"

            # Calculate the converted amount
            result = many_pet * conversion_rates[pet_type]
            
            # Ask the user if they want to calculate the cost
            calc_cost = input("Do you want to calculate the cost? (yes/no): ")
            if calc_cost.lower() in ['yes', 'y',"نعم","ش","a"]:
                cost = many_pet * cost_rates[pet_type]
                print(f"The equivalent number of {pet_type} pets is: {result} and the cost is {cost} Gems.")
            else:
                print(f"The equivalent number of {pet_type} pets is: {result}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

cal()
