import pytest
import pandas as pd

@pytest.fixture(scope='session')
def pandas_series_fixture():
    data = [1, 4, 6, 7, 2, 6, 80, 8, 10, 33, 789, 23, 67, 102]
    return pd.Series(data)

@pytest.fixture(scope='session')
def pandas_dataframe_fixture():
    data = {'col1': [1, 2, 3, 4], 'col2': [1, 2, 3, 4]}
    return pd.DataFrame(data)
    
@pytest.fixture(scope='session')
def key_vault_vame():
    return 'arnts-keyvault'

@pytest.fixture(scope='session')
def secret_name():
    return 'secret-for-testing'

@pytest.fixture(scope='session')
def csv_files_to_stack():
    files = ['tests\Fixtures\example_sheet_1.csv',
             'tests\Fixtures\example_sheet_2.csv']
    return files

@pytest.fixture(scope='session')
def stacked_csv_file():
    return 'tests\Fixtures\stacked_example.csv'
    