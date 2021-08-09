import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd

from graph import country_data, country_vaccinations_data


def stack_bar_chart(dataframe, title, xlabel, ylabel):
    date = pd.to_datetime(df['date'])

    plt.style.use('ggplot')

    # plot data
    fig, ax = plt.subplots(figsize=(15, 7))
    ax.bar(date, df['people_vaccinated'])
    ax.bar(date, df['people_fully_vaccinated'])
    # set ticks every week
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    # format date
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))

    return plt
