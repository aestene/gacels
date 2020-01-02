import pytest
from src.aesLib.DataScience import DataFrameTools as dft

def test_getIdxmaxIntegerPosOfSeries(pandasSeriesFixture):
    maxIndex = dft.getIdxmaxIntegerPosOfSeries(pandasSeriesFixture)
    assert maxIndex == 10
