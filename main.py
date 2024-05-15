import mplfinance as mpf
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import datetime as dt
import numpy as np

# Enable interactive mode
plt.ion()


# Initialize sample data
def create_initial_data():
    dates = pd.date_range(start="2023-05-01", periods=5, freq="D")
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

# Create a figure and axis for the plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title("Real-Time Candlestick Chart")

# Plot initial data
mpf.plot(df, type="candle", volume=True, ax=ax)


# Function to update the data and plot
def update(frame):
    global df

    # Simulate new data
    last_date = df.index[-1]
    new_date = last_date + dt.timedelta(days=1)
    new_data = {
        "Open": np.random.uniform(100, 110),
        "High": np.random.uniform(110, 115),
        "Low": np.random.uniform(95, 100),
        "Close": np.random.uniform(100, 110),
        "Volume": np.random.randint(1000, 2000),
    }
    new_df = pd.DataFrame(new_data, index=[new_date])

    # Update the original DataFrame
    df = df.append(new_df)

    # Clear the previous plot
    ax.clear()

    # Plot the updated data
    mpf.plot(df, type="candle", volume=True, ax=ax)
    ax.set_title("Real-Time Candlestick Chart")


# Create animation
ani = FuncAnimation(fig, update, interval=2000)

# Display the plot
plt.show()

# Keep the plot open
plt.ioff()
plt.show()
