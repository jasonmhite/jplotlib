import numpy as np

def rescale_viewport_for_artists(fig, ax, artists):
    """
    Use this to fix plot bounds after drawing text over the top. Probably works
    for other artists too.

    Derived from https://stackoverflow.com/questions/11545062/matplotlib-autoscale-axes-to-include-annotations

    fig, ax = subplots()
    ax.plot(...)
    l1 = ax.annotate(...)
    l2 = ax.annotate(...)
    rescale_viewport_for_artists(fig, ax, [l1, l2]) 
    """
    fig.canvas.draw_idle() # Force a redraw to update the canvas
    
    bbox = np.array([
        a.get_window_extent(fig.canvas.get_renderer()).transformed(ax.transData.inverted()).corners()
        for a in artists
    ])
    
    ax.update_datalim(
        np.row_stack(bbox)
    )
    
    ax.autoscale_view()        
