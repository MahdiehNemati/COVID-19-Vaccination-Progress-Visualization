def get_data_by_iso(dataframe, iso_name: str):
    csv_data = dataframe.loc[dataframe['iso_code'] == iso_name]

    return csv_data


def get_distinct_vaccines_company(dataframe):
    return dataframe['vaccine'].unique()


def get_data_by_vaccine_name(dataframe, vaccine_name: str):
    csv_data = dataframe.loc[dataframe['vaccine'] == vaccine_name]

    return csv_data
