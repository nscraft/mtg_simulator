from math import comb


def hypergeom_pmf(N, K, n, k):
    """Calculate the probability of drawing exactly k successes."""
    return (comb(K, k) * comb(N - K, n - k)) / comb(N, n)


def hypergeom_cdf(N, K, n, k):
    """Calculate the probability of drawing k or less successes."""
    return sum(hypergeom_pmf(N, K, n, ki) for ki in range(k + 1))


def hypergeom_sf(N, K, n, k):
    """Calculate the probability of drawing more than k successes."""
    return 1 - hypergeom_cdf(N, K, n, k)


# Parameters
N = 100  # Population size
K = 10  # Number of successes in population
n = 10  # Sample size
k = 2  # Number of successes for calculations

# Calculate probabilities for each case
P_at_0 = hypergeom_pmf(N, K, n, 0)  # Hypergeometric Probability :P(= 0)
P_at_exactly_k = hypergeom_pmf(N, K, n, k)  # Hypergeometric Probability :P(= x)
P_at_most_k = hypergeom_cdf(N, K, n, k)  # Cumulative Probability :P(<= x)
P_more_than_k = hypergeom_sf(N, K, n, k)  # Cumulative Probability :P(> x)
P_at_least_k = hypergeom_sf(N, K, n, k - 1)  # Cumulative Probability :P(>= x)
P_less_than_k = hypergeom_cdf(N, K, n, k - 1)  # Cumulative Probability :P(< x)

print(f"Chance to draw 0 (k=0): {round(P_at_0 * 100, 2)}%")
print(f"Chance to draw exactly k (k={k}): {round(P_at_exactly_k * 100, 2)}%")
print(f"Chance to draw k or less (<=k): {round(P_at_most_k * 100, 2)}%")
print(f"Chance to draw more than k (>k): {round(P_more_than_k * 100, 2)}%")
print(f"Chance to draw k or more (>=k): {round(P_at_least_k * 100, 2)}%")
print(f"Chance to draw less than k (<k): {round(P_less_than_k * 100, 2)}%")
