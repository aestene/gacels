import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def plotHeatmapBetweenColumns(df: pd.DataFrame, size: tuple, savefig=False, pathAndFileName='heatmap') -> plt.axes:
    """Plot heatmap between values of multiple columns in a pandas dataframe.
    
    Arguments:
        df {pd.DataFrame} -- Pandas dataframe
        size {tuple} -- Size of output figure
    
    Keyword Arguments:
        savefig {bool} -- True to save figure (default: {False})
        pathAndFileName {str} -- Filepath specified with filename location for image (default: {'heatmap'})
    
    Returns:
        plt.axes -- Matplotlib axes object
    """
    fig = plt.figure(figsize=size)

    ax = sns.heatmap(df, vmin=-1, cmap='coolwarm', annot=True)

    if savefig:
        plt.savefig(pathAndFileName)

    return ax