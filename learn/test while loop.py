import random

guess = int(input("enter your guess between 1-10: "))
num=random.randint(1,10)
print(num)

while guess != num:
    if guess > num:
        guess = int(input("Too high! try again: "))
    elif guess < num:
        guess = int(input("Too low! try again: "))
else:
    print("you win")