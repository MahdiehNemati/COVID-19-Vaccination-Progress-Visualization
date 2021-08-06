def get_data_by_iso(df, iso_name: str):
    csv_data = df.loc[df['iso_code'] == iso_name]

    return csv_data
