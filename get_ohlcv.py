import csv
from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("apiKey")
api_secret = os.getenv("secretKey")

client = Client(api_key, api_secret)

klines = client.get_historical_klines(
    "BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "1 Dec, 2017", "21 May, 2024"
)

csvfile = open("ohlcv_binance.csv", "w", newline="")
candlestick_writer = csv.writer(csvfile, delimiter=",")
candlestick_writer.writerow(
    ["open_time", "open", "high", "low", "close", "volume", "close_time"]
)

for kline in klines:
    temp = kline[0:7]
    # print(temp)
    candlestick_writer.writerow(temp)
    # print(kline)

print(len(klines))
