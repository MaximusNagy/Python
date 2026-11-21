print("\n*** Welcome to the multiplication table ***")

number = int(input("Enter the number: "))
print (f"\nMultiplication table for {number}: \n")
for i in range(1,11):
    print(f"{number} x {i} = {number * i}")