def subfigure_multilabel(
    fig,
    xlabel=None,
    ylabel=None,
    xpad=20,
    ypad=30,
    return_ax=False,
):
    # Common labels for subfigures

    ax = fig.add_subplot(111, frameon=False)
    ax.tick_params(axis="both", labelcolor='none', top='off', bottom='off', left='off', right='off')
    ax.grid(False, axis='both')

    if xlabel is not None:
        ax.set_xlabel(xlabel, labelpad=xpad)
    if ylabel is not None:
        ax.set_ylabel(ylabel, labelpad=ypad)

    ax.xaxis.set_ticks([])
    ax.yaxis.set_ticks([])

    if return_ax:
        return ax

def ax_labelright(
    ax,
    label,
    labelpad=0,
    return_ax=False,
):
    # Hack a "title" onto the right side of a figure
    ax_t = ax.twinx()
    ax_t.yaxis.set_label_position("right")
    ax_t.set_ylabel(label, labelpad=labelpad)
    ax_t.yaxis.set_ticks_position('none')
    ax_t.yaxis.set_ticklabels([])

    if return_ax:
        return ax_t
