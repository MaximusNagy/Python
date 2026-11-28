import qrcode

# --- بيانات شبكة WiFi ---
ssid = "Leader Gaming"  # اسم الشبكة
password = "01226477350Mk/****"  # كلمة المرور
encryption = "WPA"  # نوع التشفير (WPA/WPA2/WEP)
hidden = "true"  # "true" إذا كانت الشبكة مخفية، "false" إذا كانت مرئية

# صياغة بيانات الـ WiFi بالتنسيق القياسي
wifi_data = f"WIFI:S:{ssid};T:{encryption};P:{password};H:{hidden};;"

# --- إنشاء الـ QR Code ---
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(wifi_data)
qr.make(fit=True)

# إنشاء الصورة وحفظها
img = qr.make_image(fill_color="black", back_color="white")
img.save("wifi_qrcode.png")

# عرض الصورة
img.show()

print("✅ تم إنشاء QR Code لشبكة WiFi وحفظه باسم wifi_qrcode.png")