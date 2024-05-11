import asyncio
import websockets
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from dotenv import load_dotenv
import os

from utils import convertStringToNumber  # async def getBTCpriceUsd():

#     url = "https://api.coincap.io/v2/assets/bitcoin"
#     headers = {
#         "Accepts": "application/json",
#         "Authorization": "Bear 93e68853-017e-4931-b953-96eac7267310",
#         "Accept-Encoding": "gzip, deflate, br",
#     }
#     session = Session()
#     session.headers.update(headers)

#     try:
#         response = session.get(url)
#         data = response.json()

#         # Access the 'data' dictionary and then access its keys
#         return data["data"]["priceUsd"]
#     except (ConnectionError, Timeout, TooManyRedirects) as e:
#         print(e)
bear = os.getenv("COINCAP_KEY")


async def getCadRate():
    url = "https://api.coincap.io/v2/rates/canadian-dollar"
    headers = {
        "Accepts": "application/json",
        "Authorization": "Bear {bear}",
        "Accept-Encoding": "gzip, deflate, br",
    }
    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url)
        data = response.json()

        # Access the 'data' dictionary and then access its keys
        return data["data"]["rateUsd"]
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


async def get_BTC_to_CAD():
    async with websockets.connect(
        "wss://ws.coincap.io/prices?assets=bitcoin"
    ) as websocket:
        while True:
            try:
                # Receive data from the WebSocket
                response = await websocket.recv()
                data = json.loads(response)

                # Extract relevant data (BTC price in USD)
                btc_price_usd = data["bitcoin"]

                # Get CAD rate (simulated function)
                cad_rate = await getCadRate()

                # Calculate BTC to CAD conversion
                btc_to_cad = convertStringToNumber(
                    btc_price_usd
                ) / convertStringToNumber(cad_rate)
                # print("BTC to CAD:", btc_to_cad)

                yield btc_to_cad

            except Exception as e:
                print("Error:", e)


async def get_BTC_to_USD():
    async with websockets.connect(
        "wss://ws.coincap.io/prices?assets=bitcoin"
    ) as websocket:
        while True:
            try:
                # Receive data from the WebSocket
                response = await websocket.recv()
                data = json.loads(response)

                # Extract relevant data (BTC price in USD)
                btc_price_usd = data["bitcoin"]

                # print("BTC to USD:", convertStringToNumber(btc_price_usd) / 1.0013)
                yield convertStringToNumber(btc_price_usd)

            except Exception as e:
                print("Error:", e)


async def get_BTC_History(interval, start, end):
    url = "https://api.coincap.io/v2/assets/bitcoin/history?interval={interval}?start={start}&end={end}"
    headers = {
        "Accepts": "application/json",
        "Authorization": "Bear {bear}",
        "Accept-Encoding": "gzip, deflate, br",
    }
    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url)
        data = response.json()

        # Access the 'data' dictionary and then access its keys
        return data["data"]
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
