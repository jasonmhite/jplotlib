from jplotlib.plot_types.radar_plot import *
from jplotlib.plot_types.histogram import *
from jplotlib.plot_types.spectra import *
from jplotlib.plot_types.multilabel import *
from jplotlib.plot_types.waterfall import *
from jplotlib.plot_types.count_plot import bar_counts

try:
    from jplotlib.plot_types.confusion import plot_relative_color_confusion_matrix
except ImportError:
    pass
