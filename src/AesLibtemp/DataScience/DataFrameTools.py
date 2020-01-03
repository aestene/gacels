"""Tools to manipulate Pandas DataFrames for Data Science tasks.
"""
import pandas as pd

def setRowsToDisplayPandas(rows: int):
    """Set the number of rows Pandas will display when showing a DataFrame.

    Arguments:
        rows {int} -- Number of rows.
    """
    pd.options.display.max_rows = rows

def getIdxmaxIntegerPosOfSeries(series: pd.Series) -> int:
    """Get the index of the largest entry in a Pandas series as an integer.

    Arguments:
        series {pd.Series} -- Series

    Returns:
        int -- Integer index of maximum value
    """
    currentIndex = 0
    maxIndex = 0
    maxValue = 0
    for value in series:
        if value > maxValue:
            maxValue = value
            maxIndex = currentIndex
        currentIndex += 1
    return maxIndex
