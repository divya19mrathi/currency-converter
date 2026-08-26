import json
from pathlib import Path


class CurrencyConverter:
    def __init__(self, rates_file):
        self.rates_file = Path(rates_file)
        self.rates = self._load_rates()

    def _load_rates(self):
        with open(self.rates_file, "r") as file:
            return json.load(file)

    def convert(self, from_currency, to_currency, amount):
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency not in self.rates:
            raise ValueError(f"Unsupported currency code: {from_currency}")

        if to_currency not in self.rates[from_currency]:
            raise ValueError(f"Unsupported currency conversion: {from_currency} to {to_currency}")

        if amount < 0:
            raise ValueError("Amount cannot be negative.")

        rate = self.rates[from_currency][to_currency]

        return amount * rate