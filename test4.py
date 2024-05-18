import streamlit as st
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import time


# Function to generate random candlestick data
def generate_data():
    time_index = pd.date_range(start="1/1/2022", periods=100, freq="T")
    data = pd.DataFrame(index=time_index)
    data["Open"] = np.random.rand(100) * 100
    data["Close"] = data["Open"] + (np.random.rand(100) - 0.5) * 10
    data["High"] = data[["Open", "Close"]].max(axis=1) + np.random.rand(100) * 5
    data["Low"] = data[["Open", "Close"]].min(axis=1) - np.random.rand(100) * 5
    return data


# Initialize the data
data = generate_data()

# Streamlit application
st.title("Real-Time Candlestick Chart")

# Placeholder for the candlestick chart
candlestick_chart = st.empty()


# Function to update the chart
def update_chart():
    global data
    new_data = generate_data()
    data = pd.concat([data, new_data])
    fig = go.Figure(
        data=[
            go.Candlestick(
                x=data.index,
                open=data["Open"],
                high=data["High"],
                low=data["Low"],
                close=data["Close"],
            )
        ]
    )
    candlestick_chart.plotly_chart(fig)


# Initial rendering
update_chart()

# Periodically update the chart
while True:
    time.sleep(5)
    update_chart()
    st.experimental_rerun()
