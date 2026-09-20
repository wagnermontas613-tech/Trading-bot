import yfinance as yf
import time
import requests

TELEGRAM_TOKEN = "8829635133:AAGdQMUTkLVdO-VpGLnn-s8VOxSSzcfKlBs"
CHAT_ID = "5305936007"

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def get_signal():
    return None

send_telegram("✅ BOT MACHE BAZ!")
