import sys

# Ask the user to set a password
password = input("Enter your password: ")
while True:
    password_check = input("Re-enter your new app password: ")
    if password == password_check:
        print("Password saved!")
        break
    else:
        print("Password incorrect, try again.")

# Get user's name
name = input("Now, let me know your name\nEnter your name: ")
print(f"Name saved! Nice to meet you, {name}")

# Get user's age
age = input("Enter your age: ")
while True:
    if age.isdigit():
        age = int(age)
        if age >= 18:
            print("You are in!")
            break
        else:
            print("You have to be 18+.")
            sys.exit()
    else:
        print("You did not enter a valid age.")
        age = input("Enter your age: ")

# Get user's email
email = input("Enter your Email: ")
print("Email saved!")

# Get email password
email_password = input("Enter your email password: ")
print("Email password saved!")

# Store user information
infos = [name, age, email, email_password]
infos_labels = ["Name", "Your age", "Your Email", "Your Email password"]

# Retrieve stored information
while True:
    info_choice = input("I got your: (name/age/email/email password), what do you want to know? ").strip().lower()
    pass_input = input("Enter your app password: ")

    if pass_input == password:
        if info_choice == "name":
            print(f"Your name is: {infos[0]}")
        elif info_choice == "age":
            print(f"Your age is: {infos[1]}")
        elif info_choice == "email":
            print(f"Your email is: {infos[2]}")
        elif info_choice == "email password":
            print(f"Your email password is: {infos[3]}")
        else:
            print("Invalid choice. Try again.")
    else:
        print("Password incorrect.")
