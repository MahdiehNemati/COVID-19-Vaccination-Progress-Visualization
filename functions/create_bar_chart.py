
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd


def bar_chart(dataframe, title, ylabel, xlabel):
    dataframe.loc[0:, "date"] = pd.to_datetime(dataframe['date'])
    dataframe.set_index('date', inplace=True)

    # set ggplot style
    plt.style.use('ggplot')

    # plot data
    fig, ax = plt.subplots(figsize=(15, 7))
    ax.bar(dataframe.index, dataframe['daily_vaccinations'])
    # set ticks every week
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    # format date
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))

    ax.set_title(title)
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)

    return plt
