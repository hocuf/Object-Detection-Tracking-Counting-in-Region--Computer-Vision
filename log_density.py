import datetime
import pandas as pd
import os

def log_density(count, threshold=10):
    """
    Logs the density of people in a specific area by comparing the count to a predefined threshold.

    This function creates a log entry indicating whether the density of people at a specific time
    is considered "intense" or "rare" based on the provided count and threshold. The log is saved
    to a CSV file, which includes the date, time, person count, and density status for each entry.

    Args:
    - count: The current count of people detected.
    - threshold: The threshold for determining if the density is considered "intense". Defaults to 10.

    Returns:
    - df: A DataFrame containing the log entry for the current time step.

    Details:
    - The function retrieves the current date and time, formats them, and uses these values to create a log entry.
    - "Density" status is determined based on whether the count exceeds the specified threshold.
    - A new row is added to a CSV file ('density_log.csv') for each invocation of the function. If the CSV file does not exist, it is created; if it does, the new data is appended.
    - The CSV file's header is included only if the file is being created for the first time.
    """
    # Get current date and time
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    # Determine density status based on the count and threshold
    density_status = "intense" if count >= threshold else "rare"

    # Create a DataFrame for the log entry
    data = {
        "Date": [date],
        "Time": [time],
        "Person": [count],
        "Density": [density_status]
    }
    df = pd.DataFrame(data)

    # Append the log entry to the CSV file, creating it if necessary
    df.to_csv('density_log.csv', mode='a', header=not os.path.exists('density_log.csv'), index=False)

    return df
