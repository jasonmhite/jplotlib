# JPlotLib

This is a set of miscellaneous tools I wanted to put in one place. Mostly stuff I use repeatedly,
especially plots, so that I can easily have them at hand. More functions to come...

## Installing...

Current dependencies:

  * Matplotlib
  * Seaborn

To install:

* Option 1: clone and install (obviously you need git installed)
  
  ```bash
  git clone https://github.com/jasonmhite/jplotlib.git
  cd jplotlib
  python ./setup.py install
  ```

* Option 2: pip from Github

  ```bash
  pip install git+https://github.com/jasonmhite/jplotlib.git
  ``` 
## Modules...

### `set_plot_style`

This is the figure style I tend to use. It's basically the same as the `whitegrid` style in
Seaborn, but with a few tweaks:

* `figure.figsize` is set to 8in x 6in, so figures are bigger
* `figure.dpi` and `savefig.dpi` are set to 150, which makes figures higher resolution
* `legend.fancybox`, `legend.frameon` and `legend.shadow` are turned on, to make
  legends prettier
* `axes.formatter.useoffset` is turned off, which disables the annoying scientific-notation
  offset on figures (note: you can still have scientific notation, it just doesn't do that
  stupid offset business automatically)

It works kind of like Seaborn in that it tweaks settings when imported. Since it messes with
stuff, you have to *explicitly* import the submodule; it's not exported by default. It also
must be done **after** Matplotlib and Seaborn. Something like:

```python
import matplotlib.pyplot as plt
import seaborn as sb

from jplotlib import set_plot_style
```

The module doesn't export any functionality, so importing it is all you do.

### `embiggen`

Very simple, importing this just sets MPL `figure.figsize` to (15, 10). Useful
on HiDPI displays, which can sometimes make MPL figures look tiny.

### `plot_types`

Specialized types of plots...

* `radar_plot`
  
  Radar plots are kind of a PITA in MPL. This module hopefully eases that. Something like:

  ```python
  # A single chart

  import matplotlib.pyplot as plt
  from numpy import *
  from jplotlib.plot_types import radar
 
  NUM = 10
  radii = random.rand(NUM)
  labels = arange(NUM)

  fig = plt.figure()
  ax = radar(radii)
  ax.set_varlabels(labels)
  fig.show()
  ```

  ```python
  # More elaborate example with multiple charts

  import matplotlib.pyplot as plt
  import seaborn as sb
  from numpy import *
  from jplotlib.plot_types import radar, radar_axes
  from jplotlib import set_plot_style

  NUM = 10
  radii_1 = random.rand(NUM)
  radii_2 = random.rand(NUM)
  labels = arange(NUM) 

  fig = plt.figure()

  # Set up a common axes object to plot on
  _, ax = radar_axes(NUM) # First argument is thetas if you need them

  for i, data in enumerate([radii_1, radii_2]):
      radar(data, ax=ax, label="Data {}".format(i))

  # Prettify
  ax.set_rmax(1.1)
  ax.set_varlabels(labels)
  ax.set_yticklabels([])

  ax.spines["polar"].set_visible(False) # Hide the ugly border
  ax.legend()

  fig.show()
  ```

  * `spectra`

  Plot radiation spectra as time series. Includes 3D slices and a crude
  waterfall diagram.

  Note that Matplotlib is a bit buggy with axis labels in time. Especially
  with the waterfall diagram, getting the axes in terms of time does not
  seem to work correctly. 

### `incremental_stats`

An implementation of Welford's algorithm for efficiently computing the mean and variance
of a list of samples incrementally i.e., first 2 samples, then 3 samples and 
so on.

This algorithm is an online one so it far more efficient than the naive
approach, but it can still be fairly slow in pure Python. If you have Numba installed,
it will be used to generate JIT compiled versions that are much faster, otherwise
the module will fall back on the pure Python implementation. 

```python
import numpy as np
from jplotlib.incremental_stats import calc_running_stats

X = np.random.randn(100000)
mean, var, sample_var = calc_running_stats(X)
```
