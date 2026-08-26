import unittest
from src.converter import CurrencyConverter


class TestCurrencyConverter(unittest.TestCase):

    def setUp(self):
        self.converter = CurrencyConverter("rates.json")

    def test_usd_to_eur(self):
        result = self.converter.convert("USD", "EUR", 100)
        self.assertEqual(result, 85.0)

    def test_usd_to_inr(self):
        result = self.converter.convert("USD", "INR", 100)
        self.assertEqual(result, 9524.0)

    def test_negative_amount(self):
        with self.assertRaises(ValueError):
            self.converter.convert("USD", "EUR", -100)

    def test_unsupported_currency(self):
        with self.assertRaises(ValueError):
            self.converter.convert("XYZ", "EUR", 100)

    def test_unsupported_conversion(self):
        with self.assertRaises(ValueError):
            self.converter.convert("USD", "JPY", 100)


if __name__ == "__main__":
    unittest.main()