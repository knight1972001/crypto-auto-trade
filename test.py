import matplotlib.pyplot as plt
import numpy as np

# Activate interactive mode
plt.ion()

# Create empty plot
fig, ax = plt.subplots()
(line,) = ax.plot([], [], "o-", label="Dynamic Data")

# Set plot labels and title
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_title("Dynamic Plot")

# Initialize data
x_data = []
y_data = []


# Update function to be called with new data
def update_plot(new_x, new_y):
    x_data.append(new_x)
    y_data.append(new_y)
    line.set_xdata(x_data)
    line.set_ydata(y_data)
    ax.relim()  # Recalculate axes limits
    ax.autoscale_view()  # Update axes limits
    fig.canvas.draw()  # Redraw the plot


# Simulate dynamic data update
for i in range(100):
    x_new = i
    y_new = np.random.rand()
    update_plot(x_new, y_new)
    plt.pause(0.1)  # Pause to update the plot

# Keep the plot open
plt.ioff()
plt.show()
