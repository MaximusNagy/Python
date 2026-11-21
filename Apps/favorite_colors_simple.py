colors =[]

color_append = input("Add the first color you like: ")

colors.append(color_append)

answer = input("Do you want add another color you Like yes, or No: ").lower()

if answer == "yes" :
    color_another_append = input("Add another color you Like: ")
    colors.append(color_another_append)
    print(colors)

elif answer == "no":
    print(colors)

else:
    print("Please choose [Yes, or No]")
