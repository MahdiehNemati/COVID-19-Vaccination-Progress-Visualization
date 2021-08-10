import pandas as pd

from functions.create_bar_chart import bar_chart
from functions.get_data_by_iso import get_data_by_iso

country_vaccinations_data = pd.read_csv('data/country_vaccinations.csv')

country_data = get_data_by_iso(country_vaccinations_data, 'AFG')

country_data_chart_title = ('Daily Vaccinations Progress of the {country_name} in 2021').format(
    country_name=country_data.iloc[0]['country'])

country_data_chart = bar_chart(dataframe=country_data, title=country_data_chart_title, ylabel='Daily Vaccinations',
                               xlabel="Date")

country_data_chart.show()


