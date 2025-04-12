from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import logging
from dotenv import load_dotenv
import os

# تحميل المتغيرات من ملف .env
load_dotenv()

# جلب التوكن من ملف .env
BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update, context):
    update.message.reply_text('مرحباً! أنا بوت الطيارة.')

def button(update, context):
    # أكواد اللعبة أو التفاعل هنا
    pass

def main():
    # تهيئة البوت
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
