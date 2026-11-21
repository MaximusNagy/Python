def show_balance(balance):
    print(f"Your balance is ${balance} ") 

def deposit(balance):
    amount = float(input("Enter the deposit:"))
    if amount < 0:
        print("That's not valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    print("*****************************")
    amount = float(input("Enter the withdraw:"))
    print("*****************************")
    if amount > balance:
        print("*****************************")
        print("Insufficient funds")
        print("*****************************")
        return 0
    elif amount < 0 :
        print("*****************************")
        print("Amount must be greater than zero")
        print("*****************************")
        return 0

    else:
        return amount
def main():
    balance = 0
    is_running = True

    while is_running:
        print("*****************************")

        print("\n---banking program---\n")
        print("1. show_balance")
        print("2. deposit")
        print("3. withdraw")
        print("4. Exit")
        print("*****************************")
        ATM_process = input("Enter your choice: ")
        if ATM_process == "1":
            show_balance(balance)
        elif ATM_process == "2":
            balance += deposit(balance)
        elif ATM_process == "3":
            balance -= withdraw(balance)
        elif ATM_process == "4":
            print("*****************************")
            print("Thanks using program bank, Good Bye!")
            print("*****************************")
            break
        else:
            print("*****************************")
            print("\nThat is not a vallid choice\n")
            print("*****************************")

if __name__== '__main__':
    main()