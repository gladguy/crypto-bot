from app import app, TradingBot
from config import Config

if __name__ == "__main__":
    config = Config("config.yaml")
    bot = TradingBot(config)
    bot.run()