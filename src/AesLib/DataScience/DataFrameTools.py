"""Tools to manipulate Pandas DataFrames for Data Science tasks.
"""
import pandas as pd

def setRowsToDisplayPandas(rows: int):
    """Set the number of rows Pandas will display when showing a DataFrame.

    Arguments:
        rows {int} -- Number of rows.
    """
    pd.options.display.max_rows = rows

def printDataFrame(dataFrame: pd.DataFrame, maxRows=5, maxColumns=7, width=None):
    with pd.option_context(
            'display.max_rows', maxRows,
            'display.max_columns', maxColumns,
            'display.width', width):
        print(dataFrame)

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

def readCsvFiles(csvFiles: list) -> list:
    csvDataFrames = []
    for filename in csvFiles:
        dataFrame = pd.read_csv(filename, sep=';')
        csvDataFrames.append(dataFrame)
    return csvDataFrames

def stackCsvFiles(csvFiles: list, writeTofile=False) -> pd.DataFrame:
    csvDataFrames = readCsvFiles(csvFiles)
    stackedDataFrame = pd.concat(csvDataFrames, axis=0, ignore_index=True)
    stackedDataFrame.drop(stackedDataFrame.columns[0], axis=1, inplace=True)
    if writeTofile:
        stackedDataFrame.to_csv('stacked-dataframe.csv', sep=';', index=False)

    return stackedDataFrame

def checkForColumnsWithNoDataOrVariation(dataFrame: pd.DataFrame):
    description = dataFrame.describe().T
    print("N Total columns         : {}".format(len(description)))
    print("N Cols with no data     : {}".format(len(description.loc[description['count'] == 0])))
    print("N Cols with no variation: {}".format(len(description.loc[description['std'] == 0])))
