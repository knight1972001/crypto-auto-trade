import mplfinance as mpf
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import datetime as dt
import numpy as np

# Enable interactive mode
plt.ion()


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


# Initialize the DataFrame
df = create_initial_data()

# Create a figure and axes for the plot
fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(10, 8), gridspec_kw={"height_ratios": [3, 1]}
)
ax1.set_title("Real-Time Candlestick Chart")

# Plot initial data
mpf.plot(df, type="candle", ax=ax1, volume=ax2)


# Function to update the data and plot
def update(frame):
    global df

    # Simulate new data for each second
    last_date = df.index[-1]
    new_date = last_date + dt.timedelta(seconds=1)
    new_data = {
        "Open": np.random.uniform(100, 110),
        "High": np.random.uniform(110, 115),
        "Low": np.random.uniform(95, 100),
        "Close": np.random.uniform(100, 110),
        "Volume": np.random.randint(1000, 2000),
    }
    new_df = pd.DataFrame(new_data, index=[new_date])

    # Update the original DataFrame
    df = pd.concat([df, new_df])

    # Get the current view limits
    xlim = ax1.get_xlim()
    ylim1 = ax1.get_ylim()
    ylim2 = ax2.get_ylim()

    # Clear the previous plots
    ax1.clear()
    ax2.clear()

    # Plot the updated data
    mpf.plot(df, type="candle", ax=ax1, volume=ax2)
    ax1.set_title("Real-Time Candlestick Chart")

    # Restore the previous view limits
    ax1.set_xlim(xlim)
    ax1.set_ylim(ylim1)
    ax2.set_ylim(ylim2)


# Create animation
ani = FuncAnimation(
    fig, update, interval=5000, cache_frame_data=False
)  # Update interval set to 5 seconds

# Display the plot
plt.show()

# Keep the plot open
plt.ioff()
plt.show()
