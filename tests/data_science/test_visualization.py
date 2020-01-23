import os

from src.gacels.data_science import visualization as vis

def test_plot_heatmap_between_columns_save_figure(pandas_dataframe_fixture):
    size = (10, 10)
    
    savefig = True

    filename = 'test-figure.png'

    _ = vis.plot_heatmap_between_columns(pandas_dataframe_fixture, size, savefig, filename)

    assert os.path.isfile(filename)

    os.remove(filename)
