import pandas as pd

def setRowsToDisplayPandas(rows: int):
    pd.options.display.max_rows = rows

def getIdxmaxIntegerPosOfSeries(s: pd.Series) -> int:
    """Get the index of the largest entry in a Pandas series as an integer. 
    
    Arguments:
        s {pd.Series} -- Series
    
    Returns:
        int -- Integer index of maximum value
    """
    current_index = 0
    max_index = 0
    max_value = 0
    for c in s:
        if c > max_value:
            max_value = c
            max_index = current_index
        current_index += 1
    return max_index