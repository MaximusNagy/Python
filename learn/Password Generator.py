import random
import string

# رسالة ترحيبية
print("=" * 50)
print("🔐 Welcome to the Password Generator! 🔐".center(50))
print("=" * 50)

# أخذ المدخلات من المستخدم
try:
    len_pass = int(input("Enter the total number of characters in the password: "))
    len_letters = int(input("Enter the number of letters: "))
    len_numbers = int(input("Enter the number of numbers: "))
    len_symbols = int(input("Enter the number of symbols: "))

    # التحقق من صحة المجموع
    if (len_letters + len_numbers + len_symbols) == len_pass:
        print("\n✅ Generating your secure password...\n")

        # توليد مكونات كلمة المرور
        random_letters = random.choices(string.ascii_letters, k=len_letters)
        random_numbers = random.choices(string.digits, k=len_numbers)
        random_symbols = random.choices(string.punctuation, k=len_symbols)

        # دمج المكونات وخلطها
        password_chars = random_letters + random_numbers + random_symbols
        random.shuffle(password_chars)

        # تحويل القائمة إلى نص
        password = ''.join(password_chars)
        print("🔑 Your Generated Password is:", password)
    else:
        print("\n❌ Invalid input. The sum of letters, numbers, and symbols does not match the total length.")
except ValueError:
    print("\n⚠️ Please enter valid numeric values only.")
