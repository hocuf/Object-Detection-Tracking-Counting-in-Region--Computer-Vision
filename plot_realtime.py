import matplotlib.pyplot as plt
from IPython.display import clear_output
counts = []
def plot_realtime(count, window=50):
    """
        Plots the number of people detected in real-time over a sliding window.

        This function updates a global list with the latest count of detected people and plots
        the counts over a specified window of time. It is designed to provide a real-time visualization
        of how the number of people in a specific area changes over time.

        Args:
        - count: The current count of people detected.
        - window: The number of time steps to display on the plot. Defaults to 50.

        Details:
        - `counts` is a global list that stores the count of people detected at each time step.
        - This list is updated with the latest count, and only the most recent `window` counts are kept.
        - A line plot is generated showing the variation in the number of people over the specified window.
        - The plot is titled "Real-time Person Count" and includes labels for both the X-axis (Time) and Y-axis (Number of People).
        - The Y-axis is dynamically adjusted based on the maximum count within the current window to ensure all data points are visible.

        Note:
        - `clear_output(wait=True)` is used to clear the previous plot before displaying the new one, allowing for a dynamic update effect.
        - This function requires `matplotlib` for plotting and `IPython.display.clear_output` for dynamically updating the plot in a Jupyter Notebook or similar environments.
    """

    global counts  # Access the global list of counts
    counts.append(count)  # Update the list with the latest count
    counts = counts[-window:]  # Keep only the latest 'window' number of counts

    plt.figure(figsize=(10, 6))
    plt.plot(counts)  # Plot the counts
    plt.title("Real-time Person Count")  # Title of the plot
    plt.xlabel("Time")  # X-axis label
    plt.ylabel("Number of People")  # Y-axis label
    plt.ylim(0, max(counts) + 10)  # Adjust Y-axis limits
    plt.show()
    clear_output(wait=True)  # Clear the output to update the plot with the latest data