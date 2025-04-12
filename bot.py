from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# بيانات المستخدم
users = {}

# فحص الرصيد
def check_balance(user_id):
    if user_id not in users:
        users[user_id] = {"balance": 0}
    return users[user_id]["balance"]

# أمر بدء
def start(update, context):
    keyboard = [
        [InlineKeyboardButton("🏆 حسابي", callback_data='balance')],
        [InlineKeyboardButton("💸 شحن رصيد", callback_data='recharge')],
        [InlineKeyboardButton("🚀 العب الطيارة", callback_data='play')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("أهلاً بيك في البوت! اختر ما تود فعله:", reply_markup=reply_markup)

# عرض الرصيد
def show_balance(update, context):
    user_id = update.message.from_user.id
    balance = check_balance(user_id)
    update.message.reply_text(f"رصيدك الحالي: {balance} نقاط")

# الشحن
def recharge(update, context):
    keyboard = [
        [InlineKeyboardButton("💳 فودافون كاش", callback_data='vodafone')],
        [InlineKeyboardButton("💳 إنستا باي", callback_data='instapay')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("اختر طريقة الشحن:", reply_markup=reply_markup)

# اختيار فودافون كاش
def vodafone(update, context):
    update.callback_query.answer()
    update.callback_query.message.reply_text("تم اختيار فودافون كاش. يرجى إرسال رقم المعاملة بعد الدفع.")

# اختيار إنستا باي
def instapay(update, context):
    update.callback_query.answer()
    update.callback_query.message.reply_text("تم اختيار إنستا باي. يرجى إرسال رقم المعاملة بعد الدفع.")

# بداية اللعب
def play(update, context):
    update.message.reply_text("اللعبة ستبدأ الآن!")

# التعامل مع الأزرار
def button(update, context):
    query = update.callback_query
    if query.data == 'balance':
        show_balance(update, context)
    elif query.data == 'recharge':
        recharge(update, context)
    elif query.data == 'vodafone':
        vodafone(update, context)
    elif query.data == 'instapay':
        instapay(update, context)
    elif query.data == 'play':
        play(update, context)

def main():
    updater = Updater("7742479143:AAHb0SfmbjmCW7slNh7o1-mShJXesTNguEE", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
