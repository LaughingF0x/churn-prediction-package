import unittest
import pandas as pd
from churnpkg import churn_probability_for_customer
import os


class TestChurnPkg(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        DATA_PATH = os.path.join(BASE_DIR, "data", "data_merged_with_probs.csv")

        cls.df = pd.read_csv(DATA_PATH)

    def test_highest_greater_than_lowest(self):
        highest_id = 15653251
        lowest_id = 15662641

        p_high = churn_probability_for_customer(self.df, highest_id)
        p_low = churn_probability_for_customer(self.df, lowest_id)

        self.assertGreater(p_high, p_low)

    def test_raises_if_customer_missing(self):
        with self.assertRaises(ValueError):
            churn_probability_for_customer(self.df, -999999)


if __name__ == "__main__":
    unittest.main()