import unittest
from src.validator import validate_transaction


class TestValidator(unittest.TestCase):

    def test_valid_transaction(self):
        transaction = {
            "transaction_id": "T001",
            "quantity": "2",
            "unit_price": "150"
        }

        result = validate_transaction(transaction)

        # TODO : Vérifier que result est True


    def test_negative_quantity(self):
        transaction = {
            "transaction_id": "T002",
            "quantity": "-3",
            "unit_price": "150"
        }

        result = validate_transaction(transaction)

        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()