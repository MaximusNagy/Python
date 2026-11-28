import random

# رسومات الجلاد
hangman_pics = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

print("\n**** Welcome to Hangman Game ****")

# توليد الكلمة
words = ["hello", "world", "python"]
word = (random.choice(words))
guess = 6
hied_word = list("-" * len(word))
used_letters = []

while guess > 0:
    print(hangman_pics[6 - guess])  # عرض الرسمة حسب عدد الأخطاء
    print("Word to guess:", ''.join(hied_word))
    print("Used letters:", ', '.join(used_letters))
    print(f"Tries left: {guess}")

    guess_player = input("\nEnter your guess: ").lower()

    if len(guess_player) != 1 or not guess_player.isalpha():
        print("Please enter a single valid letter.")
        continue

    if guess_player in used_letters:
        print(f"You already guessed '{guess_player}'. Try another letter.")
        continue

    used_letters.append(guess_player)

    if guess_player in word:
        print("✅ Correct guess!")
        for i in range(len(word)):
            if word[i] == guess_player:
                hied_word[i] = guess_player

        if '-' not in hied_word:
            print("\n🎉 Congratulations! You win!")
            print("The word was:", word)
            break
    else:
        guess -= 1
        print("❌ Wrong guess.")

if guess == 0:
    print(hangman_pics[-1])
    print("\n💀 You lost! The word was:", word)
