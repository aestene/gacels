# pylint: skip-file
import os
import datetime as dt
import pandas as pd

#from AesLib.DataEngineering.Bazefield import downloadDataFromBazefieldAsCSV
from aeslib.data_science import dataframe_tools as dft
from aeslib.data_science.interval_analysis import IntervalAnalysis
from aeslib.data_engineering import bazefield as bf
from aeslib.data_engineering import azure_tools as at
from aeslib.data_science import missing_data_analysis as mda

def download_data():
    from_timestamp = dt.datetime(year=2017, month=10, day=1)
    to_timestamp = dt.datetime(year=2017, month=10, day=1)
    interval = '10'
    aggregates = 'Min,Max,Average,End,Standard deviation'
    keyvault = at.AzureKeyvaultHelper(key_vault_name='arnts-keyvault')

    turbines_re_string = 'DOW-[a-zA-Z_]\d{2}-(StateRun|ActivePower|ActivePowerLimit|ReactivePower|NacelleDirection|WindSpeed|OilLevel|ActualWindDirection_mean|AmbientTemp|BladeAngle|BladeAngleRef|Forecast-Available)(U|V|W|$|A|B|C)'
    calc_re_string = 'DOW-[a-zA-Z_]\d{2}-CALC-(TheoreticalProduction)($)'
    meteorological_re_string = 'DOW-F000-Met-THP-(AirTemp|AirHumidity)$'
    weather_forecast_re_string = 'DOW-EFS-(WindSpeed|WindDir|WaveDir|CurrentSpeed|CurrentDir)($|-10m|-40m|-110m)'

    reg_ex_strings = [turbines_re_string, calc_re_string, meteorological_re_string, weather_forecast_re_string]
    
    destination = '../Data/'
    bazefield_client = bf.BazefieldClient(keyvault=keyvault,
                                          from_timestamp=from_timestamp,
                                          to_timestamp=to_timestamp,
                                          reg_ex_strings=reg_ex_strings,
                                          aggregates=aggregates,
                                          interval=interval,
                                          destination=destination)
    bazefield_client.download_data_from_bazefield_as_csv()

def process_data_frames():
    csv_files = os.listdir('data/')
    csv_files = ['data/' + filename for filename in csv_files]
    dft.stack_csv_files(csv_files)

if __name__ == '__main__':

    print('end')
