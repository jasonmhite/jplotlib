# Initially inspired by https://stackoverflow.com/questions/15240003/matplotlib-intelligent-axis-labels-for-timedelta
import matplotlib as mpl
import datetime as dt

def time_ticker(
    offset=dt.timedelta(seconds=0), # Offset, as a timedelta
    t0=None, # If a datetime, will be formated relative to this otherwise as a timedelta
    trans=lambda t: t, # Arbitrary transform applied to data
    fmt="%d %b %Y %H:%M:%S", # Only used if datetime
):
    """
    Set axis:
        ax.(x|y)axis.set_major_formatter(time_ticker(...))

    Probably also want to rotate the ticks:
        ax.tick_params(axis='x', rotation=90)
    """
    if t0 is None:
        fmt_is_datetime = False
        T_start = dt.timedelta(seconds=0)
    else:
        fmt_is_datetime = True
        T_start = t0
    
    def formatter(t, pos):
        ti = dt.timedelta(seconds=trans(t)) + offset + T_start
        
        if fmt_is_datetime:
            return ti.strftime(fmt)
        else:
            return str(ti)
        
    return mpl.ticker.FuncFormatter(formatter)

