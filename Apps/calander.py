import calendar
from datetime import date

# الحصول على تاريخ اليوم
today = date.today()
yy, mm, dd = today.year, today.month, today.day

# إنشاء التقويم للشهر الحالي
cal = calendar.monthcalendar(yy, mm)

# طباعة اسم الشهر والسنة
print(f"\n📅  {calendar.month_name[mm]} {yy}\n")

# طباعة أسماء الأيام
days = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
print(" ".join(days))

# طباعة الأسابيع مع تمييز اليوم الحالي
for week in cal:
    for day in week:
        if day == 0:
            print("  ", end=" ")  # طباعة فراغ للأيام الفارغة
        elif day == dd:
            print(f"\033[1;31m{day:2}\033[0m", end=" ")  # تلوين اليوم الحالي بالأحمر
        else:
            print(f"{day:2}", end=" ")  # طباعة الأيام العادية
    print()  # سطر جديد لكل أسبوع
