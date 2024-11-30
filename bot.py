import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я работаю через Webhook!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Я могу ответить на команды /start и /help.")

if __name__ == "__main__":
    # Замените "ВАШ_ТОКЕН" на токен вашего бота
    BOT_TOKEN = os.getenv("BOT_TOKEN")

    # Создайте приложение
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Добавьте обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Настройте Webhook
    PORT = int(os.environ.get("PORT", 8443))  # Порт, предоставленный Render
    WEBHOOK_URL = f"https://{os.environ['RENDER_EXTERNAL_HOSTNAME']}/webhook/{BOT_TOKEN}"

    # Запускаем приложение через Webhook
    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        webhook_url=WEBHOOK_URL,
    )
