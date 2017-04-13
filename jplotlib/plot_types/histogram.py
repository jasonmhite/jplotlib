import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

__all__ = ["spineless_histogram"]

def spineless_histogram(data, ax=None, line=None, linecolor=None, linealpha=0.5, *args, **kwargs):
    if line == "mean":
        line = np.mean(data)

    if linecolor is None:
        linecolor = "red"

    if ax is None:
        ax = plt.gca()

    ax.hist(np.asarray(data), *args, **kwargs)
    ax.set_yticks([])
    sb.despine(ax=ax, top=True, right=True, left=True)

    if line is not None:
        ax.axvline(line, color=linecolor, alpha=0.5)
