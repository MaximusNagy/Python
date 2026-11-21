import os
import shutil
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS
from tkinter import filedialog, messagebox
import tkinter as tk

def get_image_date(file_path):
    try:
        image = Image.open(file_path)
        info = image._getexif()
        if info:
            for tag, value in info.items():
                tag_name = TAGS.get(tag, tag)
                if tag_name == "DateTimeOriginal":
                    return datetime.strptime(value, "%Y:%m:%d %H:%M:%S")
    except Exception:
        pass
    
    timestamp = os.path.getmtime(file_path)
    return datetime.fromtimestamp(timestamp)

def start_organizing():
    # إخفاء نافذة tkinter الرئيسية
    root = tk.Tk()
    root.withdraw()

    # طلب اختيار مجلد المصدر
    source_dir = filedialog.askdirectory(title="اختر المجلد الذي يحتوي على الصور")
    if not source_dir:
        return

    # طلب اختيار مجلد الوجهة
    dest_dir = filedialog.askdirectory(title="اختر المكان الذي تريد تنظيم الصور فيه")
    if not dest_dir:
        return

    extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.heic')
    files = [f for f in os.listdir(source_dir) if f.lower().endswith(extensions)]

    if not files:
        messagebox.showinfo("تنبيه", "لا توجد صور مدعومة في هذا المجلد.")
        return

    for filename in files:
        file_path = os.path.join(source_dir, filename)
        date_obj = get_image_date(file_path)
        
        folder_name = date_obj.strftime("%Y-%m-%d")
        new_folder_path = os.path.join(dest_dir, folder_name)
        
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)

        time_prefix = date_obj.strftime("%H-%M-%S_")
        new_filename = time_prefix + filename
        new_path = os.path.join(new_folder_path, new_filename)

        shutil.copy2(file_path, new_path)
    
    messagebox.showinfo("تم العمل", f"تم تنظيم {len(files)} صورة بنجاح!")

if __name__ == "__main__":
    start_organizing()