import pandas as pd
import os

def load_data(uploaded_file=None):
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        df.to_csv("data/uploaded_data.csv", index=False)
        return df
    elif os.path.exists("data/other_industries_original_unaltered.csv"):
        return pd.read_csv("data/other_industries_original_unaltered.csv")
    else:
        return pd.DataFrame()
