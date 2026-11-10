
import unittest

from src.validator import validate_transaction, clean_transactions


class TestValidator(unittest.TestCase):

    def test_valid_transaction(self):
        transaction = {
            "transaction_id": "T001",
            "date": "2026-10-15",
            "quantity": "2",
            "unit_price": "150"
        }

        self.assertTrue(validate_transaction(transaction))

    def test_negative_quantity(self):
        transaction = {
            "transaction_id": "T002",
            "date": "2026-10-15",
            "quantity": "-3",
            "unit_price": "150"
        }

        self.assertFalse(validate_transaction(transaction))

    def test_zero_quantity(self):
        transaction = {
            "transaction_id": "T003",
            "date": "2026-10-15",
            "quantity": "0",
            "unit_price": "100"
        }

        self.assertFalse(validate_transaction(transaction))

    def test_invalid_quantity(self):
        transaction = {
            "transaction_id": "T004",
            "date": "2026-10-15",
            "quantity": "abc",
            "unit_price": "100"
        }

        self.assertFalse(validate_transaction(transaction))

    def test_negative_price(self):
        transaction = {
            "transaction_id": "T005",
            "date": "2026-10-15",
            "quantity": "2",
            "unit_price": "-50"
        }

        self.assertFalse(validate_transaction(transaction))

    def test_missing_price(self):
        transaction = {
            "transaction_id": "T006",
            "date": "2026-10-15",
            "quantity": "2"
        }

        self.assertFalse(validate_transaction(transaction))

    def test_duplicate_transactions(self):
        transactions = [
            {
                "transaction_id": "T001",
                "date": "2026-10-15",
                "quantity": "2",
                "unit_price": "100"
            },
            {
                "transaction_id": "T001",
                "date": "2026-10-16",
                "quantity": "3",
                "unit_price": "200"
            }
        ]

        valid, invalid = clean_transactions(transactions)

        self.assertEqual(len(valid), 1)
        self.assertEqual(len(invalid), 1)

    def test_valid_date(self):
        transaction = {
            "transaction_id": "T007",
            "date": "2026-10-15",
            "quantity": "2",
            "unit_price": "100"
        }

        self.assertTrue(validate_transaction(transaction))

    def test_invalid_date(self):
        transaction = {
            "transaction_id": "T008",
            "date": "2026-02-30",
            "quantity": "2",
            "unit_price": "100"
        }

        self.assertFalse(validate_transaction(transaction))


if __name__ == "__main__":
    unittest.main()
