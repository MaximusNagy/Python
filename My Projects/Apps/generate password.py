import random
import string
import os

FILE_NAME = "passwords.txt"

def display_menu():
    print("\n--- Welcome to the Password Generator ---")
    print("1. Generate password")
    print("2. Show password history")
    print("3. Delete a password")
    print("4. Exit")

# تحميل سجل كلمات المرور من الملف
def load_passwords():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return [line.strip().split(" | ") for line in file.readlines()]  # تقسيم الاسم وكلمة المرور
    return []

# حفظ كلمة المرور في الملف مع اسمها
def save_password(name, password):
    with open(FILE_NAME, "a") as file:
        file.write(f"{name} | {password}\n")

# تحديث الملف بعد الحذف
def update_password_file(passwords):
    with open(FILE_NAME, "w") as file:
        for name, pwd in passwords:
            file.write(f"{name} | {pwd}\n")

password_history = load_passwords()  # تحميل السجل عند بدء التشغيل

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter a name for the password: ").strip()
        if not name:
            print("Password name cannot be empty!")
            continue

        try:
            password_length = int(input("Enter the password length: "))
            if password_length < 4:
                print("Password length should be at least 4 characters")
                continue
        except ValueError:
            print("Please enter a valid number")
            continue

        # التأكد من وجود رقم وحرف ورمز على الأقل
        digits = random.choices(string.digits, k=1)
        letters = random.choices(string.ascii_letters, k=1)
        symbols = random.choices(string.punctuation, k=1)

        # تكملة باقي الحروف عشوائيًا
        remaining_length = password_length - 3
        all_chars = string.ascii_letters + string.digits + string.punctuation
        remaining = random.choices(all_chars, k=remaining_length)

        # دمج الأحرف وخلطها
        password_list = digits + letters + symbols + remaining
        random.shuffle(password_list)
        generated_password = ''.join(password_list)

        password_history.append((name, generated_password))
        save_password(name, generated_password)  # حفظ مع الاسم
        print(f"Generated Password for '{name}': {generated_password}")

    elif choice == "2":
        if password_history:
            print("\nPassword History:")
            for i, (name, pwd) in enumerate(password_history, 1):
                print(f"{i}. {name}: {pwd}")
        else:
            print("No passwords generated yet!")

    elif choice == "3":
        if not password_history:
            print("No passwords available to delete!")
            continue

        print("\nPassword History:")
        for i, (name, pwd) in enumerate(password_history, 1):
            print(f"{i}. {name}: {pwd}")

        try:
            password_delete = int(input("Enter the number of the password to delete: "))
            if 1 <= password_delete <= len(password_history):
                deleted_name, deleted_password = password_history.pop(password_delete - 1)
                update_password_file(password_history)  # تحديث الملف
                print(f"Password '{deleted_name}' deleted successfully!")
            else:
                print("Invalid number. Please choose from the list.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Please choose between 1, 2, 3, or 4")
