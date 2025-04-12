# استخدام صورة Python الرسمية من Docker Hub
FROM python:3.9-slim

# تعيين المجلد للعمل
WORKDIR /app

# نسخ الملفات إلى المجلد داخل الحاوية
COPY . /app

# تثبيت المتطلبات
RUN pip install --no-cache-dir -r requirements.txt

# إعداد متغير البيئة لتوكن البوت
ENV BOT_TOKEN=your_bot_token_here

# تشغيل البوت
CMD ["python", "bot.py"]
