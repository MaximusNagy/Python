import random

numbers = [0,1,2,3,4,5,6,7,8,9]
nums = []

length_pass = int(input("Enter length password: "))

for _ in range(length_pass):
    random_num = random.choice(numbers)
    nums.append(str(random_num))  # نحول الرقم إلى نص

random.shuffle(nums)
number = "".join(nums)
print("Your password is:", number)
