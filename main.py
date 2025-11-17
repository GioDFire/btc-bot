import requests
import time

# CONFIGURAZIONE
TELEGRAM_TOKEN = "INSERISCI_TOKEN"
TELEGRAM_CHAT_ID = "INSERISCI_CHAT_ID"

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": msg}
    requests.post(url, data=data)

def get_btc_price():
    r = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
    return float(r.json()["price"])

last_signal = None

while True:
    price = get_btc_price()

    # SEMPLICE LOGICA SEGNALI
    if price < 55000 and last_signal != "BUY":
        tp = price + 800
        sl = price - 400
        send_telegram(f"🟢 BUY BTCUSD\nPrezzo: {price}\nTP: {tp}\nSL: {sl}")
        last_signal = "BUY"

    if price > 68000 and last_signal != "SELL":
        tp = price - 800
        sl = price + 400
        send_telegram(f"🔴 SELL BTCUSD\nPrezzo: {price}\nTP: {tp}\nSL: {sl}")
        last_signal = "SELL"

    time.sleep(30)