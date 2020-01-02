import pandas as pd
import matplotlib.pyplot as plt

import aesLib.DataScience.Visualization as vis


def test_plotHeatmapBetweenColumnsReturnType():
    data = {'col1': [1, 2, 3, 4], 'col2': [1, 2, 3, 4]}
    df = pd.DataFrame(data)
    
    size = (10, 10)
    
    savefig = False

    ax = vis.plotHeatmapBetweenColumns(df, size, savefig)

    assert type(ax) is plt.Axes