import os
import datetime as dt
from src.AesLib.DataEngineering.Bazefield import downloadDataFromBazefieldAsCSV
from src.AesLib.DataScience import DataFrameTools

def downloadData():
    fromTimeStamp = dt.datetime(year=2018, month=2, day=16)
    toTimeStamp = dt.datetime(year=2018, month=11, day=1)

    downloadDataFromBazefieldAsCSV(fromTimeStamp, toTimeStamp)

def processDataFrames():
    csvFiles = os.listdir('data')
    csvFiles = ['data/' + filename for filename in csvFiles]
    DataFrameTools.stackCsvFiles(csvFiles)

if __name__ == '__main__':
    processDataFrames()
