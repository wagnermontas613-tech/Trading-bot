import telebot
import requests
import time
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 
        "🔥 BOT TRADING WAGNER LIVE 🔥\n\n"
        "Kòmand yo:\n"
        "/signal - Jwenn siyal kounya\n"
        "/btc - Pri BTC\n"
        "/gold - Pri Gold XAUUSD\n"
        "/help - Èd"
    )

@bot.message_handler(commands=['signal'])
def signal(message):
    # Analiz senp BTC
    try:
        r = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT").json()
        price = float(r['price'])
        
        # Estrateji senp (ou ka amelyore l apre)
        if price % 2 == 0:
            sig = "📈 BUY"
        else:
            sig = "📉 SELL"
            
        bot.send_message(message.chat.id, 
            f"📊 SIYAL TRADING\n\n"
            f"Pair: BTC/USDT\n"
            f"Pri: ${price:,.2f}\n"
            f"Siyal: {sig}\n"
            f"TF: M15\n"
            f"SL: 1%\nTP: 2%\n\n"
            f"⚠️ Se analiz edikatif, pa konsèy finansye!"
        )
    except:
        bot.send_message(message.chat.id, "Erè, re-eseye!")

@bot.message_handler(commands=['btc','gold'])
def price(message):
    try:
        symbol = "BTCUSDT" if "btc" in message.text else "XAUUSDT"
        # Pou Gold nou itilize BTC kòm egzanp pou kounya
        r = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT").json()
        bot.send_message(message.chat.id, f"💰 Pri BTC: ${float(r['price']):,.2f}")
    except:
        bot.send_message(message.chat.id, "Erè pri!")

bot.infinity_polling()
