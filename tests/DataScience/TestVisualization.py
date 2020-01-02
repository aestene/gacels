import pandas as pd
import matplotlib.pyplot as plt
import os

from src.AesLib.DataScience import Visualization as vis


def test_plotHeatmapBetweenColumnsSaveFigure():
    data = {'col1': [1, 2, 3, 4], 'col2': [1, 2, 3, 4]}
    df = pd.DataFrame(data)
    
    size = (10, 10)
    
    savefig = True

    filename = 'test-figure.png'

    ax = vis.plotHeatmapBetweenColumns(df, size, savefig, filename)

    assert os.path.isfile(filename) == True

    os.remove(filename)
