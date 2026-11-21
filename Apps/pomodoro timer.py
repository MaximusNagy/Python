import time
import os

def show_menu():
    print("\nChoice time for study:")
    print("1. 60 minutes study and 15 minutes rest")
    print("2. 45 minutes study and 10 minutes rest")
    print("3. 30 minutes study and 5 minutes rest")
    print("4. Exit ")

def countdown(label, duration):
    for i in range(duration, 0, -1):
        minutes, seconds = divmod(i, 60)
        print(f"{label} - The lest time  : {minutes} minutes {seconds} seconds", end="\r")
        time.sleep(1)
    print(f"\n⏳ {label} finish!")

try:
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            study_time, break_time = 60*60, 15*60
        elif choice == "2":
            study_time, break_time = 45*60, 10*60
        elif choice == "3":
            study_time, break_time = 25*60, 5*60
        elif choice == "4":
            print("👋 تم الخروج، بالتوفيق في دراستك!")
            break
        else:
            print("❌ اختيار غير صحيح، حاول مرة أخرى.")
            continue

        os.system("cls" if os.name == "nt" else "clear")  # مسح الشاشة لبدء العد التنازلي بشكل نظيف
        countdown("📚 Study time ", study_time)
        countdown("☕ rest time", break_time)

except KeyboardInterrupt:
    print("\n⏹️ تم الإيقاف بواسطة المستخدم. وداعًا!")
except ValueError:
    print("❌ الرجاء إدخال رقم صحيح.")
