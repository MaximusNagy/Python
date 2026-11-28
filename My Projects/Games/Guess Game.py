import random

def game():
    num = random.randint(1, 20)
    guess = None
    limit = 5
    out = False
    count = 0
    try:
        while count < limit and not out:  # الحلقة ستستمر حتى 5 محاولات أو الإجابة الصحيحة
            print("choce in (1-20) ")
            guess = int(input("Enter your guess: "))  # إدخال التخمين
            count += 1  # زيادة عدد المحاولات
            if guess == 222:
                print(num)
            elif guess < num:
                print("Your guess is too low.")
            elif guess > num:
                print("Your guess is too high.")
            elif guess == num :
                print("You win!")
                print("do you want play agin(yes or no):")
                play = input("enter your choice: ")
            elif count == limit:
                print("do you want play agin(yes or no):")
                play = input("enter your choice: ")
                if play == "yes":
                    game()
                else:
                    print("You win!")
                    out = True  # التوقف عند الإجابة الصحيحة
        if not out:  # إذا انتهت المحاولات ولم يتم تخمين الرقم الصحيح
            print(f"You've reached the limit! The number was {num}.")
    except ValueError:
        print("Please enter numbers only!")  # معالجة المدخلات غير الصحيحة

game()