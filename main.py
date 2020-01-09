from src.AesLib.DataEngineering.Bazefield import downloadDataFromBazefieldAsCSV

if __name__ == '__main__':

    fromTimeStamp = dt.datetime(year=2017, month=11, day=15)
    toTimeStamp = dt.datetime(year=2018, month=11, day=1)

    downloadDataFromBazefieldAsCSV(fromTimeStamp, toTimeStamp)