import time
import streamlit as st
import pandas as pd
import numpy as np
import mplfinance as mpf
from datetime import datetime, timedelta


# Initialize sample data with second-level frequency
def create_initial_data():
    dates = pd.date_range(
        start="2023-05-01 00:00:00", periods=60, freq="S"
    )  # 60 seconds of data
    data = {
        "Date": dates,
        "Open": np.random.uniform(100, 110, len(dates)),
        "High": np.random.uniform(110, 115, len(dates)),
        "Low": np.random.uniform(95, 100, len(dates)),
        "Close": np.random.uniform(100, 110, len(dates)),
        "Volume": np.random.uniform(1000, 2000, len(dates)).astype(int),
    }
    df = pd.DataFrame(data)
    df.set_index("Date", inplace=True)
    return df


# Function to update the data
def update_data(df):
    last_date = df.index[-1]
    new_date = last_date + timedelta(seconds=1)
    new_data = {
        "Open": np.random.uniform(100, 110),
        "High": np.random.uniform(110, 115),
        "Low": np.random.uniform(95, 100),
        "Close": np.random.uniform(100, 110),
        "Volume": np.random.randint(1000, 2000),
    }
    new_df = pd.DataFrame(new_data, index=[new_date])
    df = pd.concat([df, new_df])
    return df


# Function to plot candlestick chart
def plot_candlestick(df):
    fig, ax = mpf.plot(df, type="candle", returnfig=True)
    return fig


# Main Streamlit app
def main():
    st.title("Real-Time Candlestick Chart")
    st.sidebar.markdown("### Controls")
    update_interval = st.sidebar.slider(
        "Update Interval (seconds)", min_value=1, max_value=10, value=5
    )

    # Initialize the DataFrame
    df = create_initial_data()
    # Create initial plot
    fig = plot_candlestick(df)
    st.pyplot(fig)

    # Update plot in real-time
    while True:
        df = update_data(df)
        fig = plot_candlestick(df)
        st.pyplot(fig)
        st.empty()  # Clear the previous plot to prevent overlapping
        time.sleep(update_interval)


if __name__ == "__main__":
    main()
