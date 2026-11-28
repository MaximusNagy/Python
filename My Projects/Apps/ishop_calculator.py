print("\n*** Welcome to ishop calculator ***")

baskt =[]
mony = []
many_items = input("How many items are there in your baskt today?: ")
if many_items <="0":
        print("Invild! choose please enter number higher than 0 ")

elif many_items >"0":
        print("\nLet's get to counting items ...")
        for Grocery in range(1,int(many_items)+1):
                name_item =input(f"Please tell me the name of the item number {Grocery}: ")
                baskt.append(name_item)
                price_item =float(input(f"What is the price of {name_item}: "))
                mony.append(price_item)
        enter_baskt = input("Would you like to see your enter baskt items(yes,no)? : ").lower()
        if enter_baskt == "yes":
                print(baskt)
        price_enter_baskt = input("Would you like to see how mach it'll cost(yes,no)? : ").lower()
        if price_enter_baskt == "yes":
                print(f"The cost is:${sum(mony)}")
        else:
                input("press enter to exit: ")
else:
        print("Enter nubers only!")