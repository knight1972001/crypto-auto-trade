import pandas as pd
from lightweight_charts import Chart

from actionDB import *


def exit_graph(key):
    print("Exiting...")
    chart.exit()


def calculate_sma(df, period: int = 7):
    return pd.DataFrame(
        {"time": df["time"], f"SMA {period}": df["close"].rolling(window=period).mean()}
    ).dropna()


if __name__ == "__main__":

    # chart = Chart(toolbox=True)
    chart = Chart()
    # Columns: time | open | high | low | close | volume
    # df_bin = pd.read_csv("ex_data.csv")
    df_bin = pd.read_csv("ohlcv_binance.csv")

    df_bin["time"] = pd.to_datetime(df_bin["time"], unit="ms")
    # df_bin["close_time"] = pd.to_datetime(df_bin["close_time"], unit="ms")

    print(df_bin)

    # print(df_bin)
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

    # chart.resize(width=900, height=600)
    chart.set(df_bin, render_drawings=True)

    line = chart.create_line("SMA 50")
    sma_data = calculate_sma(df_bin, period=50)
    line.set(sma_data)
    # chart.horizontal_line(200, func=on_horizontal_line_move)

    # chart.hotkey("shift", "X", exit_graph)
    # connect_to_binance_ws()

    chart.show(block=True)
