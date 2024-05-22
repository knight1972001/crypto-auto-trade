import mplfinance as mpf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create initial DataFrame with a single row of dummy data
initial_data = {
    "Open": [100],
    "High": [100],
    "Low": [100],
    "Close": [100],
    "Volume": [0],
}
initial_index = [pd.Timestamp.now()]
data = pd.DataFrame(initial_data, index=initial_index)

# Create the figure and axis objects
fig, ax = plt.subplots()


# Function to simulate real-time tick data
def generate_tick():
    last_price = data["Close"].iloc[-1]
    tick = last_price + (np.random.rand() - 0.5) * 2
    return tick


# Function to update the DataFrame with new tick data
def update_ticks():
    global data

    last_index = data.index[-1]
    last_row = data.loc[last_index]
    date = pd.Timestamp.now()

    if (date - last_row.name).seconds >= 60:  # If new minute, add new row
        open_price = close_price = generate_tick()
        volume = np.random.randint(1, 1000)
        new_data = pd.DataFrame(
            {
                "Open": [open_price],
                "High": [open_price],
                "Low": [open_price],
                "Close": [close_price],
                "Volume": [volume],
            },
            index=[date],
        )
        data = data.append(new_data)
    else:  # Update the last row
        tick = generate_tick()
        data.at[last_index, "High"] = max(last_row["High"], tick)
        data.at[last_index, "Low"] = min(last_row["Low"], tick)
        data.at[last_index, "Close"] = tick
        data.at[last_index, "Volume"] += np.random.randint(1, 10)


# Update function for the animation
def update(frame):
    update_ticks()

    # Clear the axis and plot the updated data
    ax.clear()
    mpf.plot(data, type="candle", ax=ax)


# Create the animation
ani = FuncAnimation(fig, update, interval=1000)  # Update every second

plt.show()
