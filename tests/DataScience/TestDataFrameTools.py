from src.AesLib.DataScience import DataFrameTools as dft

def testGetIdxmaxIntegerPosOfSeries(pandasSeriesFixture):
    maxIndex = dft.getIdxmaxIntegerPosOfSeries(pandasSeriesFixture)
    assert maxIndex == 10
