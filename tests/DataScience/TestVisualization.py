import os
import pandas as pd

from src.AesLib.DataScience import Visualization as vis

def testPlotHeatmapBetweenColumnsSaveFigure():
    data = {'col1': [1, 2, 3, 4], 'col2': [1, 2, 3, 4]}
    dataFrame = pd.DataFrame(data)
    
    size = (10, 10)
    
    savefig = True

    filename = 'test-figure.png'

    _ = vis.plotHeatmapBetweenColumns(dataFrame, size, savefig, filename)

    assert os.path.isfile(filename)

    os.remove(filename)
