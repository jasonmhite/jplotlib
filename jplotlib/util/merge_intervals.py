from math import inf # Alt for older compat: inf = float('inf')

## Efficient implementation, O(n logn) for a sort and then linear.
def merge_intervals(L, tol=0, sorted=False):
    """
    Merge a list of overlapping intervals L=[(a1, b1), ..., (an, bn)].

    O[n log(n)] if L is not sorted, O[n] if input is already sorted (sorted=True).
    L should be a *list* of pairs, convert NumPy arrays with .tolist() first.

    Setting tol > 0 will merge "nearby" intervals if they're within `tol`.

    Algorithm from
        https://www.geeksforgeeks.org/merging-intervals/
    """

    if not sorted:
        L.sort(key=lambda a: a[0])
    # Else assume sorted

    if len(L) <= 1: return L
    
    S = [L[0]]
    
    for a, b in L[1:]:
        Sa, Sb = S[-1]
        
        if a >= Sa and a <= Sb + tol:
            S[-1] = (Sa, b)
        else:
            S.append((a, b))
            
    return S 

def expand_intervals(L, min_len, direction="c", always=False, clip_l=0, clip_r=None):
    # direction: c, l, or r -> centered, left, right
    # clip: minimum value to clip to (none to skip)
    # always: if true, always add min_len, otherwise only expand when b - a < min_len

    if len(L) == 0:
        return L
    
    if clip_l is None:
        clip_l = -inf
    if clip_r is None:
        clip_r = inf

    for i, (a, b) in enumerate(L):

        if (b - a < min_len) or always:
            if always:
                dL = min_len
            else:
                dL = min_len - (b - a)

            if direction == "c":
                a_new = max(a - dL / 2, clip_l)
                b_new = min(b + dL / 2, clip_r)
            elif direction == "r":
                a_new = a
                b_new = min(b + dL, clip_r)
            elif direction == "l":
                a_new = max(a - dL, clip_l)
                b_new = b

            L[i] = (a_new, b_new)

    return L

## Original implementation, fast enough on average but still not great
# def merge_intervals(I):
#     L = [tuple(I[0])]
    
#     for a, b in I[1:]:
#         for i, (l, r) in enumerate(L):
#             if a >= l and a <= r:
#                 L[i] = (min(a, l), max(b, r))
#                 break
#         else: L.append((a, b)) # This else belongs to the for loop!
            
#     return L 
