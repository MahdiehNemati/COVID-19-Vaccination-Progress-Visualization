def get_data_by_iso(dataframe, iso_name: str):
    csv_data = dataframe.loc[dataframe['iso_code'] == iso_name]

    return csv_data


def get_distinct_vaccines_company(dataframe):
    return dataframe['vaccine'].unique()


def get_data_by_vaccine_name(dataframe, vaccine_name: str):
    csv_data = dataframe.loc[dataframe['vaccine'] == vaccine_name]

    return csv_data


def get_vaccination_data_in_country_with_all_companies(dataframe, country_name: str):
    csv_data = dataframe.loc[dataframe['location'] == country_name]

    return csv_data


def get_distinct_vaccines_company_in_specific_country(dataframe, country):
    country_dataframe = get_vaccination_data_in_country_with_all_companies(dataframe, country)
    company_country_dataframe = get_distinct_vaccines_company(country_dataframe)

    return company_country_dataframe


def get_all_vaccines_by_company_in_specific_country(dataframe, country_name,company_name ):
    country_dataframe = get_vaccination_data_in_country_with_all_companies(dataframe, country_name)
    all_vaccine_by_company_in_country = get_data_by_vaccine_name(country_dataframe,company_name)

    return all_vaccine_by_company_in_country