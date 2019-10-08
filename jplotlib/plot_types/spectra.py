from matplotlib import pyplot as plt
from matplotlib.ticker import FixedLocator, FuncFormatter
from matplotlib.dates import date2num, DateFormatter

import seaborn as sb
import numpy as np

from mpl_toolkits.mplot3d import Axes3D
# from matplotlib.collections import PolyCollection
from matplotlib.patches import Polygon
import mpl_toolkits.mplot3d.art3d as art3d

# __all__ = []

def mk_polygon_verts(X, Y, ymin=0):
    C1 = np.atleast_2d((X[-1], ymin))
    C2 = np.atleast_2d((X[0], ymin))
    
    verts = np.column_stack((X, Y))
    
    return np.concatenate((C1, C2, verts), axis=0)

def spectrum_tsplot(
    ax, # AX MUST BE 3d projection
    spectra,
    ebins=None,
    colors=sb.color_palette(),
    alpha=0.7,
):
    n_colors = len(colors)
    n_spec = len(spectra)

    z_max = spectra.max()

    k = 0

    ind = np.arange(len(spectra))
    y_max = n_spec - 1

    if ebins is None:
        ebins = np.arange(len(spectra[0]))

    ## The zorder for this is broken and seemingly unfixable
    # if include_total:
        # Z = spectra.sum(axis=1)
        # # Scale to the current window
        # Z /= Z.max()
        # Z *= z_max / 3 # Looks better when scaled

        # l = art3d.Line3D(
            # ebins[-1] * np.ones(n_spec),
            # ind,
            # Z,
            # zorder=1,
        # )
        # ax.add_line(l) 

    for i, spec in zip(ind, spectra):
        verts = mk_polygon_verts(ebins, spec)
        P = Polygon(verts, alpha=alpha, facecolor=colors[k], edgecolor=colors[k], zorder=-1)

        # Cycle through colors
        if k >= n_colors - 1: k = 0
        else: k += 1

        ax.add_patch(P)
        art3d.pathpatch_2d_to_3d(P, z=i, zdir='y')

    ax.set_xlim([0, ebins[-1]])
    ax.set_ylim([0, y_max])
    ax.set_zlim([0, z_max])

def waterfall(
    ax,
    spectra,
    normalize_counts=False, # Scale the spectra e.g. for different live times
    interp=True,
):
    spec = spectra.copy()

    if normalize_counts:
        spec /= spec.sum(axis=1)[:, None]

    ax.imshow(
        spec,
        aspect="auto",
        interpolation="spline36" if interp else None,
    )

