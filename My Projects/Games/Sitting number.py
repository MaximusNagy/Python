import random

numbers = [0,1,2,3,4,5,6,7,8,9]

random.shuffle(numbers)

Sitting_number =random.choices(numbers, k=6)
while Sitting_number[0] ==0:
    Sitting_number =random.choices(numbers, k=6)


print("".join(str(i) for i in Sitting_number))


