import pytest
import pandas as pd

@pytest.fixture(scope='session')
def pandasSeriesFixture():
    data = [1, 4, 6, 7, 2, 6, 80, 8, 10, 33, 789, 23, 67, 102]
    return pd.Series(data)
    
@pytest.fixture(scope='session')
def pandasDataFrameFixture():
    data = {'col1': [1, 2, 3, 4], 'col2': [1, 2, 3, 4]}
    return pd.DataFrame(data)
