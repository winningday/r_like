# test_r_like.py
import unittest
from fractions import Fraction  # Add this import
from r_like import r_like

class TestRLike(unittest.TestCase):
    def test_choose(self):
        self.assertEqual(r_like.choose(52, 5), 2598960)
        self.assertEqual(r_like.choose(13, 4), 715)
        self.assertEqual(r_like.choose(13, 4, formatted=True), '715')
        self.assertEqual(r_like.choose(52,5, formatted="True"), '2,598,960')

    def test_seq(self):
        self.assertEqual(r_like.seq(1, 10), list(range(1, 11)))
        self.assertEqual(r_like.seq(1, 10, 2), list(range(1, 11, 2)))

    def test_mean(self):
        self.assertEqual(r_like.mean([1, 2, 3, 4, 5]), 3.0)

    def test_median(self):
        self.assertEqual(r_like.median([1, 2, 3, 4, 5]), 3)
        self.assertEqual(r_like.median([1, 2, 3, 4, 5, 6]), 3.5)

    def test_sd(self):
        self.assertAlmostEqual(r_like.sd([1, 2, 3, 4, 5]), 1.5811388300841898)

    def test_var(self):
        self.assertAlmostEqual(r_like.var([1, 2, 3, 4, 5]), 2.5)

    def test_sum_values(self):
        self.assertEqual(r_like.sum_values([1, 2, 3, 4, 5]), 15)

    def test_prod(self):
        self.assertEqual(r_like.prod([1, 2, 3, 4, 5]), 120)

    def test_summary(self):
        summary = r_like.summary([1, 2, 3, 4, 5])
        self.assertEqual(summary['min'], 1)
        self.assertEqual(summary['max'], 5)
        self.assertEqual(summary['mean'], 3.0)
        self.assertEqual(summary['median'], 3)
        self.assertAlmostEqual(summary['sd'], 1.5811388300841898)
        self.assertAlmostEqual(summary['var'], 2.5)
        self.assertEqual(summary['sum'], 15)
        self.assertEqual(summary['prod'], 120)
        self.assertEqual(summary['count'], 5)

    def test_fractions(self):
        self.assertEqual(r_like.fractions(0.5), Fraction(1, 2))
        self.assertEqual(r_like.fractions(2/3), Fraction(2, 3))
    

    def test_factorial(self):
        self.assertEqual(r_like.factorial(0), 1)
        self.assertEqual(r_like.factorial(1), 1)
        self.assertEqual(r_like.factorial(5), 120)
        self.assertEqual(r_like.factorial(8), 40320)
        with self.assertRaises(ValueError):
            r_like.factorial(-1)

    def test_plot(self):
        try:
            r_like.plot([1, 2, 3, 4, 5], [2, 4, 6, 8, 10], kind='line')
            r_like.plot([1, 2, 3, 4, 5], [2, 4, 6, 8, 10], kind='scatter')
            r_like.plot([1, 2, 3, 4, 5], [2, 4, 6, 8, 10], kind='bar')
        except Exception as e:
            self.fail(f"Plot function raised an exception {e}")

    def test_one_in(self):
        self.assertEqual(r_like.one_in(47/85), "approximately 1 in 2")
        self.assertEqual(r_like.one_in(33/16660), "approximately 1 in 505")
        self.assertEqual(r_like.one_in(1/3), "approximately 1 in 3")

if __name__ == '__main__':
    unittest.main()
