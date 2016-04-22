import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.spines import Spine
from matplotlib.projections.polar import PolarAxes
from matplotlib.projections import register_projection, projection_registry

__all__ = ["radar", "radar_axes"]

def _calc_theta(num_vars):
    theta = 2*np.pi * np.linspace(0, 1-1./num_vars, num_vars)
    theta += np.pi/2

    return theta

def _radar_factory(num_vars):
    theta = _calc_theta(num_vars)

    def unit_poly_verts(theta):
        x0, y0, r = [0.5] * 3
        verts = [(r*np.cos(t) + x0, r*np.sin(t) + y0) for t in theta]
        return verts

    proj_name = "radar-{}".format(len(theta))

    class RadarAxes(PolarAxes):
        # name = 'radar'
        RESOLUTION = 1

        def fill(self, *args, **kwargs):
            closed = kwargs.pop('closed', True)
            return super(RadarAxes, self).fill(closed=closed, *args, **kwargs)

        def plot(self, *args, **kwargs):
            lines = super(RadarAxes, self).plot(*args, **kwargs)
            for line in lines:
                self._close_line(line)

        def _close_line(self, line):
            x, y = line.get_data()
            # FIXME: markers at x[0], y[0] get doubled-up
            if x[0] != x[-1]:
                x = np.concatenate((x, [x[0]]))
                y = np.concatenate((y, [y[0]]))
                line.set_data(x, y)

        def set_varlabels(self, labels):
            self.set_thetagrids(theta * 180/np.pi, labels)

        def _gen_axes_patch(self):
            verts = unit_poly_verts(theta)
            return plt.Polygon(verts, closed=True, edgecolor='k')

        def _gen_axes_spines(self):
            spine_type = 'circle'
            verts = unit_poly_verts(theta)
            verts.append(verts[0])
            path = Path(verts)
            spine = Spine(self, spine_type, path)
            spine.set_transform(self.transAxes)
            return {'polar': spine}

    if proj_name not in projection_registry.get_projection_names():
        RadarAxes.name = proj_name
        RadarAxes.theta = theta
        register_projection(RadarAxes)

    return theta, proj_name

def radar_axes(nvar):
    theta, proj = _radar_factory(nvar)
    return theta, plt.axes(projection=proj)

def radar(
    r,
    ax=None,
    yticks=True,
    **kwargs
):
    nvar = len(r)

    theta, proj = _radar_factory(nvar)

    if ax is None:
        _, ax = radar_axes(nvar)

    ax.plot(theta, r, **kwargs)
    ax.set_varlabels([])

    if not yticks:
        ax.set_yticklabels([])

    return ax
