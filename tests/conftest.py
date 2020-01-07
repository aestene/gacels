import pytest
import pandas as pd

@pytest.fixture(scope='session')
def pandasSeriesFixture():
    data = [1, 4, 6, 7, 2, 6, 80, 8, 10, 33, 789, 23, 67, 102]
    return pd.Series(data)
    
@pytest.fixture(scope='session')
def keyVaultName():
    return 'arnts-keyvault'

@pytest.fixture(scope='session')
def secretName():
    return 'secret-for-testing'
