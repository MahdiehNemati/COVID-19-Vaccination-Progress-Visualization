import pandas as pd

from functions.get_data_by_iso import get_distinct_vaccines_company, get_data_by_vaccine_name, get_data_by_vaccine_name_in_country

country_vaccinations_by_manufacturer = pd.read_csv('data/country_vaccinations_by_manufacturer.csv')

company_data = get_distinct_vaccines_company(country_vaccinations_by_manufacturer)

vaccine_number_by_company = {}
for i in company_data:
    sum = 0
    all_vaccines_by_name = get_data_by_vaccine_name(country_vaccinations_by_manufacturer, i)
    for index, row in all_vaccines_by_name.iterrows():
        number = int(row['total_vaccinations'])
        sum = sum + number
    vaccine_number_by_company[i] = sum

all_vaccines_number = 0
for i, j in vaccine_number_by_company.items():
    all_vaccines_number = all_vaccines_number + j

vaccine_company_percentage = {}
for i, j in vaccine_number_by_company.items():
    vaccine_company_percentage[i] = (j / all_vaccines_number) * 100


company_country_data = get_data_by_vaccine_name_in_country(country_vaccinations_by_manufacturer, "Australia")

vaccine_number_by_company_in_country = {}
for i in company_country_data:
    sum=0
    all_vaccines_by_company = get_data_by_vaccine_name_in_country(country_vaccinations_by_manufacturer, i)
    for index, row in country_vaccinations_by_manufacturer.iterrows():
        number = int(row['total_vaccinations'])
        sum = sum + number
    vaccine_number_by_company_in_country[i] = sum

print(vaccine_number_by_company_in_country)