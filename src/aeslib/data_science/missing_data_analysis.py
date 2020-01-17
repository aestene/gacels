import missingno as msno
import pandas as pd

def plot_correlation_between_missing_data(df: pd.DataFrame):
    msno.heatmap(df)
    