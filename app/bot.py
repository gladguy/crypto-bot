from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from app.analyzer import DexAnalyzer

class TradingBot(DexAnalyzer):
    def __init__(self, config):
        super().__init__(config)
        self.tg_token = os.getenv('TELEGRAM_BOT_TOKEN')
        self.application = Application.builder().token(self.tg_token).build()
        self._register_handlers()

    def _register_handlers(self):
        self.application.add_handler(CommandHandler("start", self.start))
        self.application.add_handler(CommandHandler("buy", self.buy))
        self.application.add_handler(CommandHandler("sell", self.sell))

    async def start(self, update: Update, context):
        await update.message.reply_text("Welcome to Crypto Bot!")

    def run(self):
        self.application.run_polling()