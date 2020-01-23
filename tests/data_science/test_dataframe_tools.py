import pandas as pd

from src.gacels.data_science import dataframe_tools as dft

def test_set_rows_to_display_pandas():
    rows = 100
    dft.set_rows_to_display_pandas(rows)

    assert pd.options.display.max_rows == rows

def test_get_idxmax_integer_pos_of_series(pandas_series_fixture):
    max_index = dft.get_idxmax_integer_pos_of_series(pandas_series_fixture)
    assert max_index == 10

#def testStackCsvFiles(csvFilesToStack, stackedCsvFile):
#    stackedDataFrame = pd.read_csv(stackedCsvFile, sep=';')

#    stackedCsvFiles = dft.stackCsvFiles(csvFilesToStack)

 #   assert stackedCsvFiles.equals(stackedDataFrame)
