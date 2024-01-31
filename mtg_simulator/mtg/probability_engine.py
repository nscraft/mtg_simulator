from math import comb

# Population as N
# Num Successes in Population as K
# Sample as n
# Num Successes in Sample as k


def hypergeom_pmf(N, K, n, k):
    """Calculate the probability of drawing exactly k successes."""
    return (comb(K, k) * comb(N - K, n - k)) / comb(N, n)


def hypergeom_cdf(N, K, n, k):
    """Calculate the probability of drawing k or less successes."""
    return sum(hypergeom_pmf(N, K, n, ki) for ki in range(k + 1))


def hypergeom_sf(N, K, n, k):
    """Calculate the probability of drawing more than k successes."""
    return 1 - hypergeom_cdf(N, K, n, k)


# Hypergeometric Probability :P(= 0)
def P_at_0(N, K, n):
    return hypergeom_pmf(N, K, n, 0)


# Hypergeometric Probability :P(= x)
def P_at_exactly_k(N, K, n, k):
    return hypergeom_pmf(N, K, n, k)


# Cumulative Probability :P(<= x)
def P_at_most_k(self):
    return self.hypergeom_cdf(self.k)


# Cumulative Probability :P(> x)
def P_more_than_k(N, K, n, k):
    return hypergeom_sf(N, K, n, k)


# Cumulative Probability :P(>= x)
def P_at_least_k(N, K, n, k):
    return hypergeom_sf(N, K, n, k - 1)


# Cumulative Probability :P(< x)
def P_less_than_k(N, K, n, k):
    return hypergeom_cdf(N, K, n, k - 1)
