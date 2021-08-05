import pandas as pd

from functions.get_data_by_iso import get_data_by_iso

country_vaccinations_data = pd.read_csv('data/country_vaccinations.csv')

aus_data = get_data_by_iso(country_vaccinations_data, 'AUS')

