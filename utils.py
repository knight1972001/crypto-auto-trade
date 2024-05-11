import datetime
import pytz


def convertStringToNumber(string):
    try:
        parsed_float = float(string)
        return parsed_float
    except ValueError:
        print("Cannot parse the string as a float")


def get_time():

    # Get current timestamp
    timestamp_now = datetime.datetime.now().timestamp()

    # Convert timestamp to datetime object
    current_time = datetime.datetime.fromtimestamp(timestamp_now)

    # Get your local timezone
    your_timezone = pytz.timezone("America/New_York")

    # Convert to your local time zone
    current_time_local = current_time.astimezone(your_timezone)

    formatted_time = current_time_local.strftime("%Y-%m-%d %H:%M:%S")

    print("Current time in your timezone:", formatted_time)
