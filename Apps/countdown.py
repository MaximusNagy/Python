import time
import winsound  # استيراد مكتبة الصوت لنظام Windows

def play_sound():
    winsound.Beep(1000, 1000)  # إصدار صوت بتردد 1000 هرتز لمدة 1000 مللي ثانية (1 ثانية)

def show_menu():
    print("\nWelcome")
    print("1. Hours")
    print("2. Minutes")
    print("3. Seconds")
    print("4. Exit")

while True:
    show_menu()
    choice = input("\nEnter your choice: ")

    if choice == "4":
        print("Exiting...")
        break

    elif choice == "1":
        seconds = int(input("Please enter hours: ")) * 3600

    elif choice == "2":
        seconds = int(input("Please enter minutes: ")) * 60

    elif choice == "3":
        seconds = int(input("Please enter seconds: "))

    else:
        print("Invalid choice! Try again.")
        continue

    # بدء العد التنازلي
    for i in range(seconds, 0, -1):
        print(f"Time remaining: {i} seconds", end="\r")
        time.sleep(1)

    print("\nTime's up!")
    play_sound()  # تشغيل الصوت عند انتهاء العد التنازلي
