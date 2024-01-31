import unittest
import scipy.stats as ss


class TestHyperGeo(unittest.TestCase):

    def setUp(self):
        self.population_size = 10
        self.num_successes_in_pop = 1
        self.sample_size = 2
        self.num_successes_in_sample = 1

    def test_hypergeom(self):
        hpd = ss.hypergeom(M=self.population_size, n=self.num_successes_in_pop, N=self.sample_size)
        result = hpd.pmf(k=self.num_successes_in_sample)
        assert result == 0.2

    def test_hypergeom_almost(self):
        hpd = ss.hypergeom(M=self.population_size, n=self.num_successes_in_pop, N=self.sample_size)
        result = hpd.pmf(k=self.num_successes_in_sample)
        self.assertAlmostEqual(result, 0.2, places=2)


# Hypergeometric Probability :P(= 0)
# Hypergeometric Probability :P(= x)
# Cumulative Probability :P(<= x)
# Cumulative Probability :P(> x)
# Cumulative Probability :P(>= x)
# Cumulative Probability :P(< x)

if __name__ == '__main__':
    unittest.main()
