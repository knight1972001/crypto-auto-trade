import mplfinance as mpf
import pandas as pd

from actionDB import *

data = get_BTC_to_CAD_History()

# Convert timestamps to datetime
for item in data:
    item[0] = pd.to_datetime(item[0], unit="ms")

df = pd.DataFrame(data, columns=["Date", "Open", "High", "Low", "Close"])
df.set_index("Date", inplace=True)

mpf.plot(df, type="candle", mav=(3, 6, 9), style="charles")
mpf.show()
