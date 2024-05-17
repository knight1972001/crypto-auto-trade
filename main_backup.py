import asyncio
import time
import keyboard
import threading
from actionDB import *
from utils import *

# Define a flag variable to control each thread
stop_flags = {}


async def BTC(stop_event):
    async for price in get_BTC_to_USD():
        if stop_event.is_set():
            break
        print("Price USD:", price / 1.0013)


async def CAD(stop_event):
    async for price in get_BTC_to_CAD():
        if stop_event.is_set():
            break
        print("Price CAD:", price / 1.0013)


def run_btc_loop(stop_event):
    asyncio.run(BTC(stop_event))


def run_cad_loop(stop_event):
    asyncio.run(CAD(stop_event))


async def main():
    # Create and start two threads
    thread1_id = 1
    thread2_id = 2
    stop_flags[thread1_id] = threading.Event()
    stop_flags[thread2_id] = threading.Event()

    thread1 = threading.Thread(target=run_btc_loop, args=(stop_flags[thread1_id],))
    thread2 = threading.Thread(target=run_cad_loop, args=(stop_flags[thread2_id],))

    thread1.start()
    isBTC = True  # Initially set to True as BTC is started

    while True:
        if keyboard.is_pressed("q"):
            print("Exiting...")
            stop_flags[thread1_id].set()
            stop_flags[thread2_id].set()
            thread1.join()  # Wait for thread1 to finish
            thread2.join()  # Wait for thread2 to finish
            break
        if keyboard.is_pressed("s"):
            if isBTC:
                if not thread2.is_alive():
                    print("Switch to CAD")
                    stop_flags[thread1_id].set()
                    thread1.join()
                    thread2.start()
                    isBTC = False
            else:
                if not thread1.is_alive():
                    print("Switch to BTC")
                    stop_flags[thread2_id].set()
                    thread2.join()
                    thread1.start()
                    isBTC = True
        time.sleep(0.1)


if __name__ == "__main__":
    asyncio.run(main())


import pandas as pd
from io import StringIO

# Read the CSV data into a DataFrame
df = pd.read_csv("ohlcv.csv")

# Extract the desired columns
extracted_df = df[["open_time", "open", "high", "low", "close", "volume", "close_time"]]

# Save the extracted columns to a new CSV file
extracted_df.to_csv("extracted_data.csv", index=False)

print(extracted_df)
