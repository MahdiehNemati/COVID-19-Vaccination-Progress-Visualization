import pandas as pd

from functions.create_stack_bar_chart import stack_bar_chart
from functions.get_data_by_iso import get_data_by_iso

country_vaccinations_data = pd.read_csv('data/country_vaccinations.csv')

country_data = get_data_by_iso(country_vaccinations_data, 'AUS')

country_data_chart_title = ('Comparison of first doze and full doze in {country_name} - 2021').format(
    country_name=country_data.iloc[0]['country'])

country_data_stack_bar_chart = stack_bar_chart(dataframe=country_data, title=country_data_chart_title,
                                               ylabel='Vaccinations', xlabel='Date')

country_data_stack_bar_chart.show()
