import tkinter as tk
from tkinter import filedialog, messagebox
from pytube import YouTube

# دالة لتحميل الفيديو تلقائيًا بجودة 360p
def auto_download():
    url = url_entry.get().strip()
    path = path_label.cget("text").strip()
    
    if not url or path == "No path selected":
        messagebox.showerror("خطأ", "يرجى إدخال الرابط واختيار مسار الحفظ!")
        return

    try:
        yt = YouTube(url)
        title_label.config(text=f"عنوان الفيديو: {yt.title}")
        views_label.config(text=f"عدد المشاهدات: {yt.views}")
        
        # تحميل الفيديو بجودة 360p
        stream = yt.streams.filter(res="360p", progressive=True, file_extension="mp4").first()
        
        if not stream:
            messagebox.showerror("خطأ", "لم يتم العثور على جودة 360p!")
            return

        messagebox.showinfo("تحميل", "جاري تنزيل الفيديو بجودة 360p...")
        stream.download(output_path=path)
        messagebox.showinfo("نجاح", "تم التنزيل بنجاح!")
    
    except Exception as e:
        messagebox.showerror("خطأ", f"حدث خطأ أثناء التنزيل: {e}")

# دالة لاختيار مسار الحفظ
def select_path():
    path = filedialog.askdirectory()
    if path:
        path_label.config(text=path)

# إنشاء النافذة الرئيسية
root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("600x400")
root.resizable(False, False)

# عنوان التطبيق
header_label = tk.Label(root, text="YouTube Downloader", font=("Arial", 18, "bold"))
header_label.pack(pady=10)

# حقل إدخال الرابط
url_frame = tk.Frame(root)
url_frame.pack(pady=10)
url_label = tk.Label(url_frame, text="Video URL:", font=("Arial", 12))
url_label.pack(side=tk.LEFT)
url_entry = tk.Entry(url_frame, width=40, font=("Arial", 12))
url_entry.pack(side=tk.LEFT, padx=5)

# اختيار مسار الحفظ
path_frame = tk.Frame(root)
path_frame.pack(pady=10)
path_button = tk.Button(path_frame, text="Select Path", font=("Arial", 12), command=select_path)
path_button.pack(side=tk.LEFT)
path_label = tk.Label(path_frame, text="No path selected", font=("Arial", 12), fg="gray")
path_label.pack(side=tk.LEFT, padx=10)

# زر التنزيل التلقائي
download_button = tk.Button(root, text="Download 360p", font=("Arial", 14, "bold"), bg="green", fg="white", command=auto_download)
download_button.pack(pady=20)

# معلومات الفيديو
info_frame = tk.Frame(root)
info_frame.pack(pady=10)
title_label = tk.Label(info_frame, text="عنوان الفيديو: ", font=("Arial", 12))
title_label.pack(anchor="w")
views_label = tk.Label(info_frame, text="عدد المشاهدات: ", font=("Arial", 12))
views_label.pack(anchor="w")

# تشغيل النافذة
root.mainloop() 