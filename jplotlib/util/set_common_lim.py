def set_common_view(ax, which="both"):
    if which == "both":
        repeat = True
        which = "x"
    else:
        repeat = False
    
    if which == "x":
        sel = lambda a: (a.get_xlim, a.set_xlim)
    if which == "y":
        sel = lambda a: (a.get_ylim, a.set_ylim)

    L = min([
        min(sel(ax_i)[0]())
        for ax_i in ax.flat
    ])

    U = max([
        max(sel(ax_i)[0]())
        for ax_i in ax.flat
    ])
    
    for ax_i in ax.flat:
        sel(ax_i)[1]([L, U])
        
    if repeat:
        set_common_view(ax, which="y") 
