# cleaning.py

import pandas as pd

def load_data():
    df = pd.read_csv("data/covid_data.csv")
    return df

def clean_data(df):
   
    df['confirmed_date'] = pd.to_datetime(df['confirmed_date'])
    df['released_date'] = pd.to_datetime(df['released_date'])

    df['sex'] = df['sex'].fillna("Unknown")

    df['age'] = 2020 - df['birth_year']

    return df

def add_recovery_days(df):
    df['recovery_days'] = (df['released_date'] - df['confirmed_date']).dt.days
    return df