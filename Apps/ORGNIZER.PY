import os
import shutil
from datetime import datetime
import customtkinter as ctk
from tkinter import filedialog, messagebox

# إعدادات المظهر العام
ctk.set_appearance_mode("System")  # يتبع نظام الويندوز (Dark/Light)
ctk.set_default_color_theme("blue") # لون الأزرار الأساسي

class FileOrganizerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("منظم الملفات الذكي - الإصدار العصري")
        self.geometry("600x450")
        
        # --- تصميم الواجهة ---
        
        # العنوان الرئيسي
        self.label_title = ctk.CTkLabel(self, text="منظم الملفات الاحترافي", font=ctk.CTkFont(size=24, weight="bold"))
        self.label_title.pack(pady=20)

        # إطار اختيار المجلد
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(pady=10, padx=20, fill="x")

        self.entry_path = ctk.CTkEntry(self.frame, placeholder_text="اختر المجلد أو الصق المسار هنا...", width=350)
        self.entry_path.pack(side="left", padx=10, pady=20, expand=True, fill="x")

        self.btn_browse = ctk.CTkButton(self.frame, text="استعراض", command=self.browse_folder, width=100)
        self.btn_browse.pack(side="right", padx=10)

        # معلومات الحالة
        self.status_label = ctk.CTkLabel(self, text="جاهز للعمل", text_color="gray")
        self.status_label.pack(pady=5)

        # زر التشغيل الرئيسي
        self.btn_start = ctk.CTkButton(self, text="بدء التنظيم الآن", command=self.start_organizing, 
                                       fg_color="#2ecc71", hover_color="#27ae60", font=ctk.CTkFont(size=16, weight="bold"))
        self.btn_start.pack(pady=20)

        # منطقة عرض النتائج (Textbox)
        self.result_box = ctk.CTkTextbox(self, width=500, height=150)
        self.result_box.pack(pady=10, padx=20)
        self.result_box.configure(state="disabled")

    def log(self, message):
        """إضافة نص إلى صندوق النتائج"""
        self.result_box.configure(state="normal")
        self.result_box.insert("end", message + "\n")
        self.result_box.see("end")
        self.result_box.configure(state="disabled")

    def browse_folder(self):
        selected_path = filedialog.askdirectory()
        if selected_path:
            self.entry_path.delete(0, "end")
            self.entry_path.insert(0, selected_path)

    def start_organizing(self):
        folder_path = self.entry_path.get().strip().strip('"').strip("'")
        
        if not os.path.exists(folder_path):
            messagebox.showerror("خطأ", "المسار غير صحيح أو غير موجود!")
            return

        self.status_label.configure(text="جاري التنظيم...", text_color="#f1c40f")
        self.result_box.configure(state="normal")
        self.result_box.delete("1.0", "end")
        self.result_box.configure(state="disabled")

        # بدء عملية التنظيم
        image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp']
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        
        moved_count = 0
        
        for filename in files:
            full_file_path = os.path.join(folder_path, filename)
            file_ext = os.path.splitext(filename)[1].lower()

            # تحديد اسم المجلد
            if file_ext in image_extensions:
                stat = os.stat(full_file_path)
                date_created = datetime.fromtimestamp(stat.st_mtime)
                folder_name = date_created.strftime('%Y-%m (صور)')
            else:
                clean_name = filename.replace('-', ' ').replace('_', ' ')
                words = clean_name.split()
                if len(words) > 0:
                    first_word = words[0]
                    folder_name = first_word + " " + words[1] if len(first_word) <= 2 and len(words) > 1 else first_word
                else:
                    continue

            # إنشاء المجلد والنقل
            target_dir = os.path.join(folder_path, folder_name)
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)

            try:
                shutil.move(full_file_path, os.path.join(target_dir, filename))
                self.log(f"✅ نُقل: {filename} -> {folder_name}")
                moved_count += 1
            except Exception as e:
                self.log(f"❌ خطأ في {filename}: {e}")

        self.status_label.configure(text="اكتملت العملية!", text_color="#2ecc71")
        messagebox.showinfo("نجاح", f"تم تنظيم {moved_count} ملف بنجاح!")

if __name__ == "__main__":
    app = FileOrganizerApp()
    app.mainloop()