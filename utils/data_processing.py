import pandas as pd
from sklearn.impute import SimpleImputer

def clean_data(data):
    if data.empty:
        return "No dataset loaded. Please upload a dataset."
    imputer = SimpleImputer(strategy='most_frequent')
    data[['state', 'district', 'city']] = imputer.fit_transform(data[['state', 'district', 'city']])
    return data
