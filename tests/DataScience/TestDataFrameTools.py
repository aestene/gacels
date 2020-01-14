import pandas as pd

from src.AesLib.DataScience import DataFrameTools as dft

def testSetRowsToDisplayPandas():
    rows = 100
    dft.setRowsToDisplayPandas(rows)

    assert pd.options.display.max_rows == rows

def testGetIdxmaxIntegerPosOfSeries(pandasSeriesFixture):
    maxIndex = dft.getIdxmaxIntegerPosOfSeries(pandasSeriesFixture)
    assert maxIndex == 10

#def testStackCsvFiles(csvFilesToStack, stackedCsvFile):
#    stackedDataFrame = pd.read_csv(stackedCsvFile, sep=';')

#    stackedCsvFiles = dft.stackCsvFiles(csvFilesToStack)

 #   assert stackedCsvFiles.equals(stackedDataFrame)
