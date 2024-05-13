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
load_dotenv()
key = os.getenv("x-cg-demo-api-key")


async def getCadRate():
    url = "https://api.coincap.io/v2/rates/canadian-dollar"
    headers = {
        "Accepts": "application/json",
        "x-cg-demo-api-key": "{key}",
        "Accept-Encoding": "gzip, deflate, br",
    }
    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url)
        data = response.json()

        # Access the 'data' dictionary and then access its keys
        return data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


def get_BTC_to_CAD(coin_id="bitcoin", currency="cad", days="1"):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/ohlc?vs_currency={currency}&days={days}"
    headers = {"Accept": "application/json", "x-cg-demo-api-key": f"{key}"}
    session = Session()
    session.headers.update(headers)

    try:
        # response = session.get(url)
        # data = response.json()
        data = [
            [1715556600000, 83818.0, 84008.0, 83818.0, 83922.0],
            [1715558400000, 83888.0, 84127.0, 83888.0, 84127.0],
            [1715560200000, 84098.0, 84246.0, 84098.0, 84172.0],
            [1715562000000, 84407.0, 84407.0, 84095.0, 84095.0],
            [1715563800000, 84106.0, 84106.0, 83871.0, 84010.0],
            [1715565600000, 84060.0, 84060.0, 83759.0, 83973.0],
            [1715567400000, 84046.0, 84046.0, 83739.0, 83739.0],
            [1715569200000, 83621.0, 83639.0, 83354.0, 83354.0],
            [1715571000000, 83519.0, 83519.0, 83200.0, 83335.0],
            [1715572800000, 83172.0, 83585.0, 83172.0, 83585.0],
            [1715574600000, 83644.0, 83644.0, 83508.0, 83508.0],
            [1715576400000, 83507.0, 83538.0, 83331.0, 83406.0],
            [1715578200000, 83406.0, 83412.0, 83333.0, 83362.0],
            [1715580000000, 83320.0, 83394.0, 83183.0, 83183.0],
            [1715581800000, 83268.0, 83729.0, 83268.0, 83729.0],
            [1715583600000, 83759.0, 84065.0, 83751.0, 83964.0],
            [1715585400000, 84061.0, 84386.0, 84061.0, 84386.0],
            [1715587200000, 84373.0, 84994.0, 84261.0, 84994.0],
            [1715589000000, 85307.0, 86066.0, 85307.0, 86066.0],
            [1715590800000, 85939.0, 86134.0, 85766.0, 85886.0],
            [1715592600000, 85836.0, 86146.0, 85836.0, 86146.0],
            [1715594400000, 86331.0, 86363.0, 86204.0, 86207.0],
            [1715596200000, 86246.0, 86246.0, 85860.0, 85862.0],
            [1715598000000, 85693.0, 85693.0, 85472.0, 85678.0],
            [1715599800000, 85769.0, 85769.0, 85488.0, 85586.0],
            [1715601600000, 85606.0, 85719.0, 85606.0, 85719.0],
            [1715603400000, 85731.0, 85862.0, 85376.0, 85376.0],
            [1715605200000, 85713.0, 85797.0, 85712.0, 85797.0],
            [1715607000000, 85904.0, 86075.0, 85857.0, 86075.0],
            [1715608800000, 85879.0, 85879.0, 85578.0, 85823.0],
            [1715610600000, 85718.0, 86131.0, 85718.0, 86084.0],
            [1715612400000, 86157.0, 86157.0, 85801.0, 85835.0],
            [1715614200000, 85764.0, 86148.0, 85764.0, 86148.0],
            [1715616000000, 86156.0, 86378.0, 86117.0, 86378.0],
            [1715617800000, 86171.0, 86443.0, 86078.0, 86443.0],
            [1715619600000, 86596.0, 86596.0, 86253.0, 86413.0],
            [1715621400000, 86346.0, 86346.0, 85828.0, 85828.0],
            [1715623200000, 85775.0, 85931.0, 85710.0, 85887.0],
            [1715625000000, 85896.0, 85896.0, 85654.0, 85654.0],
            [1715626800000, 85670.0, 85804.0, 85670.0, 85749.0],
            [1715628600000, 85814.0, 86185.0, 85814.0, 86049.0],
            [1715630400000, 86122.0, 86315.0, 86122.0, 86315.0],
            [1715632200000, 86241.0, 86333.0, 86149.0, 86149.0],
            [1715634000000, 86184.0, 86251.0, 86180.0, 86180.0],
            [1715635800000, 86222.0, 86234.0, 86125.0, 86125.0],
            [1715637600000, 86068.0, 86090.0, 85917.0, 85917.0],
            [1715639400000, 85903.0, 85995.0, 85897.0, 85897.0],
            [1715641200000, 85777.0, 85880.0, 85755.0, 85858.0],
        ]
        return data
    except Exception as e:
        print(e)


def get_live_BTC():  # supppose re-fetch every 30 mins, in this simulation, try 5s instead.
    url = f"https://api.coingecko.com/api/v3/coins/bitcoin?localization=false&tickers=false&market_data=true&community_data=false&developer_data=false&sparkline=true"
    headers = {"Accept": "application/json", "x-cg-demo-api-key": f"{key}"}
    session = Session()
    session.headers.update(headers)
    try:
        # response = session.get(url)
        # data = response.json()

        # Path to the JSON file
        file_path = "data.json"

        # Load JSON data from the file
        with open(file_path, "r") as file:
            data = json.load(file)
        print(data)
        return data
    except Exception as e:
        print(e)


get_live_BTC()
