import random

def ran():
    print("\n--- choose between module ---")
    print("1. random.randint")
    print("2. random.random")

while True:
    ran()

    # التحقق من اختيار الموديل
    while True:
        choose = input("choose 1 or 2: ").strip()
        if choose in ["1", "2"]:
            break
        else:
            print("Wrong ⁉️ please choose 1 or 2")

    # التحقق من اختيار Heads أو Tails
    while True:
        choice = input("choose (Heads or Tails): ").strip().lower()
        if choice in ["heads", "tails"]:
            break
        else:
            print("Invalid guess⁉️ Please type 'Heads' or 'Tails'.")

    # تنفيذ الرمية حسب الموديل
    if choose == "1":
        num = random.randint(0, 1)
        result = "tails" if num == 1 else "heads"
    else:  # choose == "2"
        result = "tails" if random.random() > 0.5 else "heads"

    # مقارنة التخمين بالنتيجة
    print(f"Result: {result}")
    if choice == result:
        print("🎉 You guessed right!")
    else:
        print("❌ Wrong guess. Try again!")

    # هل تريد اللعب مرة أخرى؟
    again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if again == "no":
        print("Thanks for playing! 👋")
        break
