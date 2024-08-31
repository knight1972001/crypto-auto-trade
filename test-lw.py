from time import sleep
import pandas as pd
from lightweight_charts import Chart

from actionDB import *
from get_ohlcv import *


def exit_graph(key):
    print("Exiting...")
    chart.exit()


def calculate_sma(df, period: int = 7):
    return pd.DataFrame(
        {"time": df["time"], f"SMA {period}": df["close"].rolling(window=period).mean()}
    ).dropna()


if __name__ == "__main__":

    generate_new_csv_file()
    # chart = Chart(toolbox=True)
    chart = Chart()
    # Update CSV file
    # update_data()

    # Columns: time | open | high | low | close | volume
    # df_bin = pd.read_csv("ex_data.csv")
    df1 = pd.read_csv("data/ohlcv_binance.csv")

    df1["time"] = pd.to_datetime(df1["time"], unit="ms")
    # df_bin["close_time"] = pd.to_datetime(df_bin["close_time"], unit="ms")

    # chart.crosshair(
    #     mode="normal",
    #     vert_color="#FFFFFF",
    #     vert_style="dotted",
    #     horz_color="#FFFFFF",
    #     horz_style="dotted",
    # )

    # chart.legend(
    #     visible=True,
    #     font_size=14,
    #     percent=True,
    #     color_based_on_candle=True,
    #     text="Chart info: ",
    # )

    # # chart.resize(width=900, height=600)
    # chart.set(df_bin_static, render_drawings=True)

    # line = chart.create_line("SMA 50")
    # sma_data = calculate_sma(df_bin_static, period=50)
    # line.set(sma_data)

    chart.set(df1)

    chart.show()

    df1.dropna(inplace=True)  # drop not available
    df1.drop_duplicates(subset="time", inplace=True)  # drop duplicate rows
    df1.reset_index(inplace=True)  # reset index of data frame.

    # Update new chart
    filename = get_current_date_str()

    df2 = pd.read_csv(f"data/{filename}.csv")

    last_close = df1.iloc[-1]["close"]

    for i, series in df2.iterrows():
        chart.update(series)

        last_close = series["close"]
        sleep(0.1)
