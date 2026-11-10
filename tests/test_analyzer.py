import unittest

from src.analyzer import calculate_total_revenue


class TestAnalyzer(unittest.TestCase):

    def test_total_revenue(self):
        transactions = [
            {"quantity": "2", "unit_price": "100"},
            {"quantity": "1", "unit_price": "300"}
        ]

        result = calculate_total_revenue(transactions)
        self.assertEqual(result, 500)

if __name__ == "__main__":
    unittest.main()