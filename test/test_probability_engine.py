import unittest

from mtg.probability_engine import hypergeom_pmf, hypergeom_cdf, hypergeom_sf


class TestHypergeo(unittest.TestCase):

    def setUp(self):
        self.population_size = 10
        self.num_successes_in_pop = 2
        self.sample_size = 4
        self.num_successes_in_sample = 2

    # probability of more than num_successes (= 0)
    def test_hypergom_zero(self):
        result = hypergeom_pmf(N=self.population_size, K=self.num_successes_in_pop, n=self.sample_size,
                               k=0)
        self.assertEqual(result, 0.3333333333333333, "chance of zero failed")

    # probability of exactly number_successes (= k)
    def test_hypergeom_pmf(self):
        result = hypergeom_pmf(N=self.population_size, K=self.num_successes_in_pop, n=self.sample_size,
                               k=self.num_successes_in_sample)
        self.assertEqual(result, 0.13333333333333333, "pmf failed")

    # probability of num_successses or less (<= k)
    def test_hypergeom_cdf(self):
        result = hypergeom_cdf(N=self.population_size, K=self.num_successes_in_pop, n=self.sample_size,
                               k=self.num_successes_in_sample)
        self.assertEqual(result, 1.0, "cdf failed")

    # probability of more than num_successes (> k)
    def test_hypergeom_sf(self):
        result = hypergeom_sf(N=self.population_size, K=self.num_successes_in_pop, n=self.sample_size,
                              k=self.num_successes_in_sample)
        self.assertEqual(result, 0.0, "sf failed")


if __name__ == '__main__':
    unittest.main()
