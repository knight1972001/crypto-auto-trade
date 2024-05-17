import pandas as pd
from lightweight_charts.widgets import StreamlitChart

chart = StreamlitChart(width=900, height=600)

df = pd.read_csv("ohlcv.csv")
chart.set(df)

chart.load()
