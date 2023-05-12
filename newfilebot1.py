import sqlite3
import telebot

# تعريف البوت
bot = telebot.TeleBot('6228608379:AAGN6melXUYglRzvIv7tX9JyxKy_gCEyPwU')

# تعريف الاتصال بقاعدة البيانات
conn = sqlite3.connect('db.sqlite')

# تعريف المؤشر للتفاعل مع الجدول
cursor = conn.cursor()

# إنشاء جدول لتخزين بيانات المستخدم
cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')

# تعريف الأمر لإدخال بيانات المستخدم في قاعدة البيانات
@bot.message_handler(commands=['add_user'])
def add_user(message):
    # عزل معلومات المستخدم من الرسالة
    name = message.text.split()[1]
    age = message.text.split()[2]
    
    # إدخال المعلومات في جدول المستخدمين
    cursor.execute(f"INSERT INTO users (name, age) VALUES ('{name}', {age})")
    conn.commit()
    
    bot.reply_to(message, f'تمت إضافة {name} ({age} سنة) إلى قاعدة البيانات')

# تعريف الأمر لاسترداد بيانات المستخدم
@bot.message_handler(commands=['get_user'])
def get_user(message):
    # عزل معرّف المستخدم من الرسالة
    user_id = message.text.split()[1]
    
    # البحث عن المستخدم في قاعدة البيانات
    cursor.execute(f"SELECT name, age FROM users WHERE id = {user_id}")
    user = cursor.fetchone()
    
    # إرسال رسالة بناءً على النتيجة
    if user:
        name, age = user
        bot.reply_to(message, f'اسم المستخدم: {name}, العمر: {age}')
    else:
        bot.reply_to(message, 'لم يتم العثور على المستخدم')

# تشغيل البوت
bot.polling()