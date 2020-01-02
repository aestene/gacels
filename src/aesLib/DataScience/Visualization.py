import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def plotHeatmapBetweenColumns(df: pd.DataFrame, size: tuple, savefig: bool, pathAndFileName='heatmap') -> plt.axes:
    fig = plt.figure(figsize=size)

    ax = sns.heatmap(df, vmin=-1, cmap='coolwarm', annot=True)

    if savefig:
        plt.savefig(pathAndFileName)

    return ax
