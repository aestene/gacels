import os

from src.AesLib.DataScience import Visualization as vis

def testPlotHeatmapBetweenColumnsSaveFigure(pandasDataFrameFixture):
    size = (10, 10)
    
    savefig = True

    filename = 'test-figure.png'

    _ = vis.plotHeatmapBetweenColumns(pandasDataFrameFixture, size, savefig, filename)

    assert os.path.isfile(filename)

    os.remove(filename)
