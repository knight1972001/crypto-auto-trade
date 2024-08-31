import csv
from datetime import datetime
from binance.client import Client
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()
api_key = os.getenv("apiKey")
api_secret = os.getenv("secretKey")

client = Client(api_key, api_secret)


def init_data():

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
    csvfile.close()


def generate_new_csv_file():
    data = load_data_from_csv()
    # print(data[-1][0])
    klines = client.get_historical_klines(
        "BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, data[-1][0]
    )

    filename = get_current_date_str()

    if int(klines[-1][0]) != int(data[-1][0]):
        csvfile = open(f"data/{filename}.csv", "w", newline="")
        candlestick_writer = csv.writer(csvfile, delimiter=",")
        candlestick_writer.writerow(
            ["time", "open", "high", "low", "close", "volume", "close_time"]
        )
        print("Generating data file")
        for kline in klines:
            temp = kline[0:7]
            # print(temp)
            candlestick_writer.writerow(temp)
            # print(kline)
        csvfile.close()
    else:
        print("Nothing new")

    print(len(klines))


def update_merge_data():
    data = load_data_from_csv()
    # print(data[-1][0])
    klines = client.get_historical_klines(
        "BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, data[-1][0]
    )

    if int(klines[-1][0]) != int(data[-1][0]):
        # csvfile = open("ohlcv_binance.csv", "a", newline="")
        # candlestick_writer = csv.writer(csvfile, delimiter=",")
        print("Updating data")
        for kline in klines:
            temp = kline[0:7]
            # print(temp)
            # candlestick_writer.writerow(temp)
            # print(kline)
            data.append(temp)
        # csvfile.close()
    else:
        print("Nothing new")

    return data


def load_data_from_csv():
    # Initialize an empty list to store the CSV data
    data = []

    # Open the CSV file
    with open("data/ohlcv_binance.csv", newline="") as csvfile:
        # Create a CSV reader object
        csvreader = csv.reader(csvfile)

        # Loop through each row in the CSV
        for row in csvreader:
            # Append the row to the data list
            data.append(row)

    # Print the data list to verify the contents
    return data


def get_new_data_df():
    data = update_merge_data()
    # Define the column names
    columns = ["time", "open", "high", "low", "close", "volume", "close_time"]

    modified_data = data[1:]

    # print(modified_list[0])

    # Convert the array to a DataFrame
    df = pd.DataFrame(modified_data, columns=columns)

    return df


def get_current_date_str():
    # Get the current date
    today = datetime.today()

    # Format the date as "month-day-year.csv"
    formatted_date = today.strftime("%B-%d-%Y")

    return formatted_date
