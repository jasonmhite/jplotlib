import numpy as np

# def mesh_refine(X, factor):
    # return np.append(
        # np.column_stack(
            # np.linspace(X[:-1], X[1:], factor, endpoint=False)
        # ),
        # [X[-1]]
    # )

def mesh_refine(X, factor):
    return np.append(
        np.column_stack(
            np.linspace(X[:-1], X[1:], factor + 1)[:-1]
        ),
        [X[-1]]
    ) 
