import pandas as pd
from time import sleep
from lightweight_charts import Chart
from binance import ThreadedWebsocketManager
from dotenv import load_dotenv
import os
from binance.client import Client
from get_ohlcv import generate_new_csv_file, get_current_date_str

load_dotenv()
api_key = os.getenv("apiKey")
api_secret = os.getenv("secretKey")

client = Client(api_key, api_secret)

twm = ThreadedWebsocketManager(api_key=api_key, api_secret=api_secret)


def load_data_until_now():
    generate_new_csv_file()
    filename = get_current_date_str()

    df2 = pd.read_csv(f"data/{filename}.csv")
    df2["time"] = pd.to_datetime(df2["time"], unit="ms")

    # df2.drop(columns=["volume"], inplace=True)
    # Avoid wrong rendering real time.
    df2.dropna(inplace=True)
    df2.drop_duplicates(subset="time", inplace=True)
    df2.reset_index(inplace=True)
    # Avoid wrong rendering real time
    # last_close = df1.iloc[-1]["close"]

    # for i, series in df2.iterrows():
    #     chart.update(series)
    chart.set(df2, True)
    print("Finished loading data")


def get_trade_price():
    print("Got socket message")
    # Initialize the Binance client
    print("Get trade price")

    # start is required to initialise its internal loop
    twm.start()
    twm.start_trade_socket(callback=update_tick_graph, symbol="BTCUSDT")
    # twm.run()
    twm.join()


def exit_chart(key):
    print("exiting chart...")
    twm.stop()
    chart.exit()


def update_tick_graph(msg):
    result = []
    result.append(msg["E"])
    result.append(msg["p"])
    columns = ["time", "price"]
    result[1] = float(result[1])
    df = pd.DataFrame([result], columns=columns)
    df["time"] = pd.to_datetime(df["time"], unit="ms")
    for i, series in df.iterrows():
        print(f"Updating... {result[0]}")
        chart.update_from_tick(series)
    # chart.update_from_tick(df)


if __name__ == "__main__":
    chart = Chart()

    df1 = pd.read_csv("data/ohlcv_binance.csv")
    df1["time"] = pd.to_datetime(df1["time"], unit="ms")

    # df1.drop(columns=["volume"], inplace=True)

    # Avoid wrong rendering real time.
    df1.dropna(inplace=True)
    df1.drop_duplicates(subset="time", inplace=True)
    df1.reset_index(inplace=True)
    # Avoid wrong rendering real time
    chart.time_scale(seconds_visible=True)

    chart.crosshair(
        mode="normal",
        vert_color="#FFFFFF",
        vert_style="dotted",
        horz_color="#FFFFFF",
        horz_style="dotted",
    )

    chart.legend(
        visible=True,
        font_size=14,
        percent=True,
        color_based_on_candle=True,
        text="Chart info: ",
    )

    # print(df1)
    chart.set(df1, True)
    chart.hotkey("shift", "X", exit_chart)

    chart.show()

    load_data_until_now()
    get_trade_price()
