import random

print("Welcome to the Rock, Paper, Scissors game!")

rule = input("Please press Enter to continue or enter 'Help' for rules: ").capitalize()

if rule == "Help":
    print("""
Rules of Rock, Paper, Scissors:
- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock
""")

# الاختيارات
play = ["Rock", "Paper", "Scissors"]

# الرسومات
Rock = """   =======
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

Paper = """    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)"""

Scissors = """    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)"""

# ربط الرسمة بالاسم
art = {
    "Rock": Rock,
    "Paper": Paper,
    "Scissors": Scissors
}

# الكمبيوتر يختار
computer_choice = random.choice(play)

# اللاعب يختار
player_choice = input("Please choose between [Rock, Paper, Scissors]: ").capitalize()

# التحقق من صحة الإدخال
if player_choice not in play:
    print("Invalid choice. Please try again.")
else:
    # طباعة اختيار اللاعب والكمبيوتر بالرسومات
    print("\nYou chose:")
    print(art[player_choice])

    print("\nComputer chose:")
    print(art[computer_choice])

    # تحديد الفائز
    if player_choice == computer_choice:
        print("\nResult: It's a draw!")
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Scissors" and computer_choice == "Paper") or \
         (player_choice == "Paper" and computer_choice == "Rock"):
        print("\nResult: You win! 🎉")
    else:
        print("\nResult: You lose! 😢")
