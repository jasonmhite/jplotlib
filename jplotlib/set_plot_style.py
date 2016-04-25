import seaborn as sb
from matplotlib import rcParams

sb.set_style('white')

rcParams['figure.figsize'] = 8, 6
rcParams['legend.fancybox'] = True
rcParams['figure.dpi'] = 150
rcParams['savefig.dpi'] = 150
rcParams['legend.frameon'] = True
rcParams['legend.shadow'] = True

rcParams['axes.formatter.useoffset'] = False # Scientific notation
