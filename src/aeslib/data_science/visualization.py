"""Functions for visualization purposes in Data Science tasks.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import missingno as msno

def plot_heatmap_between_columns(
        df: pd.DataFrame,
        size: tuple = (7, 7),
        savefig=False,
        path_and_file_name='heatmap') -> plt.axes:
    """Plot heatmap between values of multiple columns in a Pandas dataframe.

    Arguments:
        df {pd.DataFrame} -- Pandas dataframe
        size {tuple} -- Size of output figure

    Keyword Arguments:
        savefig {bool} -- True to save figure (default: {False})
        path_and_file_name {str} -- Filepath (default: {'heatmap'})

    Returns:
        plt.axes -- Matplotlib axes object
    """
    plt.figure(figsize=size)

    axes = sns.heatmap(df, vmin=-1, cmap='coolwarm', annot=True)

    if savefig:
        plt.savefig(path_and_file_name)

    return axes

def plot_missing_intervals(df: pd.DataFrame, group_by=None):
    if group_by is not None:
        grouped = df.groupby(group_by)
        for _, group in grouped:
            msno.matrix(group)
    else:
        msno.matrix(df)
        
def plot_missing_value_column_correlation(df: pd.DataFrame):
    msno.heatmap(df)