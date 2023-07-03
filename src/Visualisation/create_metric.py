
import datetime as dt

import matplotlib
from infinopy import InfinoClient
import json
from langchain.callbacks import InfinoCallbackHandler
import matplotlib.pyplot as plt
import matplotlib.dates as md
import time

matplotlib.use('agg')


def plot(data, title):
    data = json.loads(data)

    # Extract x and y values from the data
    timestamps = [item["time"] for item in data]
    dates = [dt.datetime.fromtimestamp(ts) for ts in timestamps]
    y = [item["value"] for item in data]

    plt.rcParams['figure.figsize'] = [6, 4]
    plt.subplots_adjust(bottom=0.2)
    plt.xticks(rotation=25)
    ax = plt.gca()
    xfmt = md.DateFormatter('%Y-%m-%d %H:%M:%S')
    ax.xaxis.set_major_formatter(xfmt)

    # Create the plot
    plt.plot(dates, y)

    # Set labels and title
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.title(title)

    plt.savefig(f'src/Visualisation/images/new_plot_{title}.png')
    plt.show()


def create_metrics(client):
    response = client.search_ts("__name__", "latency", 0, int(time.time()))
    plot(response.text, "latency")

    response = client.search_ts("__name__", "error", 0, int(time.time()))
    plot(response.text, "errors")

    response = client.search_ts("__name__", "prompt_tokens", 0, int(time.time()))
    plot(response.text, "prompt_tokens")

    response = client.search_ts("__name__", "completion_tokens", 0, int(time.time()))
    plot(response.text, "completion_tokens")

    response = client.search_ts("__name__", "total_tokens", 0, int(time.time()))
    plot(response.text, "total_tokens")
