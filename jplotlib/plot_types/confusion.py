import numpy as np
from sklearn import metrics

def plot_relative_color_confusion_matrix(
    X,
    ax,
    display_labels=None,
    plt_kwargs={},
    label_relative=False,
    fix_colorbar=True,
):

    # Rows of X are true class, so sum of rows is number in the true class.
    # Normalize to these counts.
    X_n = np.einsum('ij,i->ij', X, 1. / X.sum(axis=1))

    cm = metrics.ConfusionMatrixDisplay(
        X_n,
        display_labels=display_labels # if display_labels is not None else np.arange(X.shape[0], dtype=int),
    )
    cm.plot(ax=ax, **plt_kwargs)

    # Change labels to the absolute counts
    if not label_relative:
        for I, t in np.ndenumerate(cm.text_):
            t.set_text(f"{X[I]:d}")

    # Fix the colorbar limits so the last tick draws
    if fix_colorbar:
        ax.images[-1].set_clim(0, 1)

