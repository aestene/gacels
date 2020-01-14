# pylint: skip-file
import os
import datetime as dt
import pandas as pd

from AesLib.DataEngineering.Bazefield import downloadDataFromBazefieldAsCSV
from AesLib.DataScience import DataFrameTools

def downloadData():
    fromTimeStamp = dt.datetime(year=2017, month=10, day=1)
    toTimeStamp = dt.datetime(year=2017, month=10, day=1)
    interval = '10'
    aggregates = 'Min,Max,Average,End,Standard deviation'
    keyVaultName = 'arnts-keyvault'
    turbinesReString = 'DOW-[a-zA-Z_]\d{2}-(StateRun|ActivePower|ActivePowerLimit|ReactivePower|NacelleDirection|WindSpeed|OilLevel|ActualWindDirection_mean|AmbientTemp|BladeAngle|BladeAngleRef|Forecast-Available)(U|V|W|$|A|B|C)'
    calcReString = 'DOW-[a-zA-Z_]\d{2}-CALC-(TheoreticalProduction)($)'
    meteorologicalReString = 'DOW-F000-Met-THP-(AirTemp|AirHumidity)$'
    weatherForecastReString = 'DOW-EFS-(WindSpeed|WindDir|WaveDir|CurrentSpeed|CurrentDir)($|-10m|-40m|-110m)'

    regExStrings = [turbinesReString, calcReString, meteorologicalReString, weatherForecastReString]

    downloadDataFromBazefieldAsCSV(fromTimeStamp, toTimeStamp, aggregates, interval, regExStrings, keyVaultName)

def processDataFrames():
    csvFiles = os.listdir('data')
    csvFiles = ['data/' + filename for filename in csvFiles]
    DataFrameTools.stackCsvFiles(csvFiles)

if __name__ == '__main__':
    downloadData()
