import os
import shutil

# استخدام المسار المطلق لضمان الدقة
folder_path = r"C:\Users\imagine\Downloads"

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Music": [".mp3", ".wav", ".aac"],
    "Compressed": [".zip", ".rar", ".tar", ".7z"],
    "Programs": [".exe", ".msi"]
}

for category in file_types.keys():
    os.makedirs(os.path.join(folder_path, category), exist_ok=True)

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if os.path.isfile(file_path):
        file_extension = os.path.splitext(filename)[1].lower()
        moved = False

        for category, extensions in file_types.items():
            if file_extension in extensions:
                try:
                    shutil.move(file_path, os.path.join(folder_path, category, filename))
                    moved = True
                except shutil.Error:
                    print(f"تخطى الملف: {filename} (موجود مسبقاً)")
                break
        
        # يمكنك اختيار نقل الملفات غير المعروفة أو تركها في مكانها
        if not moved and file_extension != "":
            os.makedirs(os.path.join(folder_path, "Others"), exist_ok=True)
            shutil.move(file_path, os.path.join(folder_path, "Others", filename))

print("تم تنظيم الملفات بنجاح!")