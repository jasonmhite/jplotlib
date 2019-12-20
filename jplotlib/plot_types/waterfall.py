"""
Time Series waterfall plot
"""
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
from jplotlib.util import time_ticker, mesh_refine

__all__ = ["waterfall", "waterfall_smooth"]

def waterfall2(
    ax,
    X,
    T,
    data,
): pass

def center(X):
    return X[:-1] + 0.5 * np.diff(X)

def waterfall(
    ax,
    X,
    T, # T must be in seconds! See jplotlib.util.time_ticker.
    data,
    pcolormesh_kwargs={},
):
    ax.pcolormesh(
        *np.meshgrid(X, T[::-1]),
        data[::-1],
        **pcolormesh_kwargs,
    )

def waterfall_smooth(
    ax,
    X,
    T,
    data,
    imshow_args={} # not interpolation, aspect
):
    args = imshow_args

    if "interpolation" not in args:
        args["interpolation"] = "lanczos"

    if "aspect" not in args:
        args["aspect"] = "auto"

    # Will choke if it's something other than upper or lower
    if "origin" not in args:
        args["origin"] = rcParams["image.origin"]

    ax.imshow(
        data,
        extent=(
            X[0],
            X[-1],
            T[-1] if args["origin"] == "upper" else T[0],
            T[0] if args["origin"] == "upper" else T[-1],
        ),
        **args,
    )
