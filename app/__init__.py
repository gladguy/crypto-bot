from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dex_analysis.db'
db = SQLAlchemy(app)

from app.bot import TradingBot
from app.analyzer import DexAnalyzer
from app.webui import WebUI