# pylint: skip-file
import os
import datetime as dt
import pandas as pd

#from AesLib.DataEngineering.Bazefield import downloadDataFromBazefieldAsCSV
from aeslib.data_science import dataframe_tools as dft
from aeslib.data_science import interval_analysis as ia
from aeslib.data_engineering import bazefield as bf

def download_data():
    from_timestamp = dt.datetime(year=2017, month=11, day=1)
    to_timestamp = dt.datetime(year=2018, month=11, day=1)
    interval = '10'
    aggregates = 'Min,Max,Average,End,Standard deviation'
    key_vault_name = 'arnts-keyvault'
    turbines_re_string = 'DOW-[a-zA-Z_]\d{2}-(StateRun|ActivePower|ActivePowerLimit|ReactivePower|NacelleDirection|WindSpeed|OilLevel|ActualWindDirection_mean|AmbientTemp|BladeAngle|BladeAngleRef|Forecast-Available)(U|V|W|$|A|B|C)'
    calc_re_string = 'DOW-[a-zA-Z_]\d{2}-CALC-(TheoreticalProduction)($)'
    meteorological_re_string = 'DOW-F000-Met-THP-(AirTemp|AirHumidity)$'
    weather_forecast_re_string = 'DOW-EFS-(WindSpeed|WindDir|WaveDir|CurrentSpeed|CurrentDir)($|-10m|-40m|-110m)'

    reg_ex_strings = [turbines_re_string, calc_re_string, meteorological_re_string, weather_forecast_re_string]

    bf.download_data_from_bazefield_as_csv(from_timestamp, to_timestamp, aggregates, interval, reg_ex_strings, key_vault_name)

def process_data_frames():
    csv_files = os.listdir('data/')
    csv_files = ['data/' + filename for filename in csv_files]
    dft.stack_csv_files(csv_files)

if __name__ == '__main__':
    
    download_data()

    print('end')
