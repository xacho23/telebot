from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я простой бот. Напиши /help, чтобы узнать, что я могу!")

# Команда /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Я могу ответить на команды:\n/start - Начать работу\n/help - Помощь")

# Основной блок программы
if __name__ == "__main__":
    # Замените "ВАШ_ТОКЕН" на токен вашего бота, полученный у BotFather
    import os

    BOT_TOKEN = os.getenv("BOT_TOKEN")
    
    application = ApplicationBuilder().token(BOT_TOKEN).build()


    # Добавляем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Запуск бота
    print("Бот запущен. Нажмите Ctrl+C для остановки.")
    application.run_polling()
