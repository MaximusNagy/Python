import random

# إنشاء كود عشوائي مكون من 4 أرقام
pin_code = random.randint(1000, 9999)

print("Generated code (for testing):", pin_code)  # تقدر تمسحه لو عايز تخليها سر

# إدخال المستخدم
num_player = int(input("Enter 4-digit PIN: "))

# التحقق من الطول
while True:
    if len(str(num_player)) !=4:
        print("Invalid! Please enter exactly 4 digits.")
        num_player = int(input("Enter 4-digit PIN: "))
    elif len(str(num_player)) == 4:
         break
    
if num_player == pin_code:
    print("success Pin code matched")
else:
    print ("Failure! PIN code did not match")
    print(f"The computer generatedthis PIN: {pin_code}")