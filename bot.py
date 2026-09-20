import yfinance as yf
import time
import requests
import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def get_signal():
    data = yf.download("EURUSD=X", period="5d", interval="15m")
    data['EMA9'] = data['Close'].ewm(span=9).mean()
    data['EMA21'] = data['Close'].ewm(span=21).mean()
    last = data.iloc[-1]
    prev = data.iloc[-2]
    if prev['EMA9'].values[0] < prev['EMA21'].values[0] and last['EMA9'].values[0] > last['EMA21'].values[0]:
        return f"ACHETE EURUSD {last['Close'].values[0]:.5f}"
    elif prev['EMA9'].values[0] > prev['EMA21'].values[0] and last['EMA9'].values[0] < last['EMA21'].values[0]:
        return f"VANTE EURUSD {last['Close'].values[0]:.5f}"
    return None

while True:
    try:
        s = get_signal()
        if s:
            send_telegram(s)
    except:
        pass
    time.sleep(900)
