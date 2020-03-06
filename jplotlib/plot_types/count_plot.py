import numpy as np

def bar_counts(X, ax, label_names=None, annotate_counts=True, bar_kwargs={}, text_kwargs={}):
    if label_names is not None:
        X_n = np.array([label_names[x] for x in X])
    else:
        X_n = X

    centers, counts = np.unique(X_n, return_counts=True)
    ax.barh(
        centers,
        counts,
        **bar_kwargs,
    )

    if annotate_counts:
        for i, c in enumerate(counts):
            ax.text(
                c,
                i,
                str(c),
                rotation=-90,
                va="center",
                **text_kwargs,
            )

    return centers, counts
