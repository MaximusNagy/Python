import random
import string

def generate_custom_code():
    # الحروف الثابتة (التي لا تتغير) مع وضع الأرقام في منتصفها بين C و M
    fixed_first = "C"
    fixed_last = "M"
    
    # اختيار رقمين عشوائيين (باللغة الإنجليزية)
    digits = "".join(random.choices(string.digits, k=2))
    
    # اختيار 4 حروف عشوائية كبيرة لباقي الكود
    random_letters = "".join(random.choices(string.ascii_uppercase, k=4))
    
    # دمج الأجزاء: حرف C + الرقمين + حرف M + 4 حروف عشوائية
    code = fixed_first + digits + fixed_last + random_letters
    
    return code

# تجربة طباعة الكود
print(generate_custom_code())