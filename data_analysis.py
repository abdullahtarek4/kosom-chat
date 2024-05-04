import pandas as pd
import numpy as np

from sklearn.datasets import fetch_openml

def load_boston_data():
    # Load the Boston housing dataset
    housing = fetch_openml(name="boston", as_frame=True)

    # Combine features and target into a DataFrame
    df = housing.frame

    return df





def get_summary_statistics(df):
    # Display basic summary statistics
    summary_stats = df.describe()
    return summary_stats

def get_first_few_rows(df, n=5):
    # Display the first few rows of the DataFrame
    first_few_rows = df.head(n)
    return first_few_rows
