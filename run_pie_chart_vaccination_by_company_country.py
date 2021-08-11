import matplotlib.pyplot as plt
import pandas as pd

from functions.get_data_by_iso import get_distinct_vaccines_company_in_specific_country, \
    get_all_vaccines_by_company_in_specific_country
from misc.constants import COUNTRY_VACCINATION_BY_MANUFACTURER

COUNTRY_NAME = 'Austria'

distinct_company_names_in_country = get_distinct_vaccines_company_in_specific_country(
    COUNTRY_VACCINATION_BY_MANUFACTURER,
    COUNTRY_NAME)

vaccine_number_by_company_in_country = {}

for i in distinct_company_names_in_country:
    all_vaccines_by_company_in_country = get_all_vaccines_by_company_in_specific_country(
        COUNTRY_VACCINATION_BY_MANUFACTURER, COUNTRY_NAME, i)
    sum = all_vaccines_by_company_in_country['total_vaccinations'].sum()

    vaccine_number_by_company_in_country[i] = sum

data = pd.DataFrame.from_dict(vaccine_number_by_company_in_country, orient='index')

y = data[0]

plt.pie(y, startangle=90)
plt.legend(data.index, loc="lower right")
plt.show()
