import numpy as np

# Gelman-Rubin score from PyMC
# https://github.com/pymc-devs/pymc/blob/master/pymc/diagnostics.py#L555
def gelman_rubin(x, return_var=False):
    # x is of shape m, n, k
    #  m: number of chains
    #  n: number of samples
    #  k: number of variables
    try:
        m, n = np.shape(x)
    except ValueError:
        return [gelman_rubin(np.transpose(y)) for y in np.transpose(x)]

    # Calculate between-chain variance
    B_over_n = np.sum((np.mean(x, 1) - np.mean(x)) ** 2) / (m - 1)

    # Calculate within-chain variances
    W = np.sum(
        [(x[i] - xbar) ** 2 for i,
         xbar in enumerate(np.mean(x,
                                   1))]) / (m * (n - 1))

    # (over) estimate of variance
    s2 = W * (n - 1) / n + B_over_n

    if return_var:
        return s2

    # Pooled posterior variance estimate
    V = s2 + B_over_n / m

    # Calculate PSRF
    R = V / W

    return np.sqrt(R)

# Warning: SLOOOOOW for large number of samples
# Could numbafy but not worth it right now
def incremental_gr(X, start, stepsize, stop=None):
    L = []
    
    N_s = X.shape[1]
    if stop is None:
        index = np.arange(start, N_s, stepsize)
    else:
        index = np.arange(start, stop, stepsize)
    
    for i in index:
        L.append(
            gelman_rubin(X[:, :i, :])
        )
        
    return index, np.asarray(L)
