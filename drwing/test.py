from turtle import *
import math

# إعداد الخلفية والسرعة
bgcolor("black")
speed(0)

# دالة لحساب نقاط القلب
def heart_points(t):
    x = 16 * math.sin(t) ** 3
    y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
    return x * 10, y * 10  # تكبير الحجم

# رسم القلب باللون الأحمر
color("red")
width(2)
penup()
goto(0, -100)
pendown()
begin_fill()

for i in range(0, 628, 2):  # رسم القلب بالكامل
    x, y = heart_points(i / 100)
    goto(x, y)

end_fill()

# رسم الصليب فوق القلب باللون الأبيض
color("white")
width(10)

# رسم الخط الأفقي للصليب
penup()
goto(-50, 0)
pendown()
forward(100)

# رسم الخط العمودي للصليب
penup()
goto(0, 50)
setheading(270)  # ضبط الاتجاه للأسفل
pendown()
forward(100)

done()
