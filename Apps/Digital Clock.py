import tkinter as tk
from time import strftime

def update_time():
    current_time = strftime('%I:%M:%S %p')  # تعديل التنسيق لعرض 12 ساعة مع AM/PM
    current_date = strftime('%Y-%m-%d')
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    root.after(1000, update_time)

# إنشاء نافذة التطبيق
root = tk.Tk()
root.title("Digital Clock")
root.geometry("500x250")
root.configure(bg='black')

# عرض الوقت
time_label = tk.Label(root, font=('Arial', 40, 'bold'), fg='red', bg='black')
time_label.pack()

# عرض التاريخ
date_label = tk.Label(root, font=('Arial', 20), fg='white', bg='black')
date_label.pack()

# تحديث الوقت تلقائياً
update_time()

# تشغيل التطبيق
root.mainloop()