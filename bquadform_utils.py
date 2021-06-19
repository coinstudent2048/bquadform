# Miscellaneous utilities for bquadform.py
#
# Use this code only for prototyping

# integer square root (floor)
# source: https://stackoverflow.com/a/53983683
def isqrt(n):
    if not isinstance(n, int):
        raise TypeError("input is not integer")
    if n > 0:
        x = 1 << (n.bit_length() + 1 >> 1)
        while True:
            y = (x + n // x) >> 1
            if y >= x:
                return x
            x = y
    elif n == 0:
        return 0
    else:
        raise ValueError("input is negative")

# integer square root (ceiling)
def isqrt_ceil(n):
    if n == 0:
        return 0
    else:
        return 1 + isqrt(n - 1)

# Euclidean division: always ensures that
# 0 <= r < |b| regardless of sign of divisor
def divmod_euclid(a, b):
    q, r = divmod(a, b)   # divmod uses floor division
    if r < 0:
        q += 1
        r -= b
    return (q, r)

# extended Euclidean algorithm
# reference: Algorithm 1.3.6 (p.16) of Cohen -
# "A Course in Computational Algebraic Number theory" (GTM 138)
def ext_euclid(a, b):
    # [Initialize]
    u = 1
    d = a
    if b == 0:
        v = 0
        return (u, v, d)
    v1 = 0
    v3 = b
    # [Finished?]
    while v3 != 0:
        # [Euclidean step]
        q, t3 = divmod(d, v3)   # a & b are assumed non-negative
        t1 = u - q * v1
        u = v1
        d = v3
        v1 = t1
        v3 = t3
    # [Finished?] cont.
    v = (d - a * u) // b
    return (u, v, d)

# extended partial Euclidean algorithm
# referece: Sub-algorithm PARTEUCL(a, b) (p. 248) of Cohen -
# "A Course in Computational Algebraic Number theory" (GTM 138)
def part_euclid(a, b, L):
    # [Initialize]
    v = 0
    d = a
    v2 = 1
    v3 = b
    z = 0
    # [Finished?]
    while abs(v3) > L:
        # [Euclidean step]
        q, t3 = divmod_euclid(d, v3)
        t2 = v - q * v2
        v = v2
        d = v3
        v2 = t2
        v3 = t3
        z += 1
    # [Finished?] cont.
    if z % 2 == 1:
        v2 = -v2
        v3 = -v3
    return (v, d, v2, v3, z)

# TODO: implement Lehmer variants for ext_euclid and part_euclid
# the Lehmer variants will replace original, but don't delete the originals
# instead, rename the originals as "ext_euclid_orig" and "part_euclid_orig"