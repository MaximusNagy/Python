import string

letters = string.ascii_lowercase  # كل الحروف الإنجليزية الصغيرة

blade = input("Enter the message: ").lower()  # نحولها لحروف صغيرة
shift = int(input("Enter shift value: "))  # عدد الحروف اللي هيتحول بيها كل حرف

encrypted = ""

for char in blade:
    if char in letters:
        index = letters.index(char)
        shifted_index = (index + shift) % 26  # %26 عشان نلف لو عدينا آخر حرف
        encrypted += letters[shifted_index]   # نحط الحرف المشفّر
    else:
        encrypted += char  # لو مش حرف إنجليزي نسيبه زي ما هو

print("Encrypted message:", encrypted)
