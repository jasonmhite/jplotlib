import numpy as np
try: 
    import numba as nb
    jit = nb.jit

except ImportError:
    import warnings
    warnings.warn("Failed to load Numba, falling back on Python implementation")
    # Dummy jit decorator with the same prototype
    jit = lambda *args, **kwargs: (lambda x: x) 

# Welford's algorithm, straight from wikipedia
# https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Welford's_online_algorithm  

__all__ = ["calc_incremental_stats"]

agg_type = nb.types.UniTuple(nb.float64, 3)

update_sig = agg_type(agg_type, nb.float64)
@jit(update_sig, nopython=True)
def update(existingAggregate, newValue):
    (count, mean, M2) = existingAggregate
    count += 1 
    delta = newValue - mean
    mean += delta / count
    delta2 = newValue - mean
    M2 += delta * delta2

    return (count, mean, M2)

finalize_sig = nb.types.UniTuple(nb.float64, 3)(agg_type)
@jit(finalize_sig, nopython=True)
def finalize(existingAggregate):
    (count, mean, M2) = existingAggregate
    (mean, variance, sampleVariance) = (mean, M2/count, M2/(count - 1)) 
    if count < 2:
        return (np.nan, np.nan, np.nan)
    else:
        return (mean, variance, sampleVariance) 

# Wrapper for the above two functions, just pass it a list of data and you'll
# get back an array with the first column being incremental mean and the
# second variance
calc_incremental_stats_sig = nb.float64[:, :](nb.float64[:])

# Note, this only works for a vector, have not generalized it to operate 
# multiple variables
@jit(calc_incremental_stats_sig, nopython=True)
def calc_incremental_stats(X):
    """
    Calculate the incremental mean and variance of vector X. That is,
    the first two moments of the first 2 samples, first 3 samples, etc.

    Returns a matrix of dimension (3, len(X) - 1). Row 1 is the incremental
    mean, row 2 is the variance, row 3 is the *sample* variance.
    """

    agg = (1.0, X[0], 0.0)

    L = np.empty((len(X) - 1, 3), dtype=np.float64)
    
    for i, x in enumerate(X[1:]):
        agg = update(agg, x)
        L[i] = finalize(agg)
        
    # Transpose it so you can unpack the result
    return L.T
