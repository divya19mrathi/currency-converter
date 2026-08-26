# Part 1: Simple Currency Converter

# Fixed exchange rate
# 1 USD = 95.24 INR

exchange_rate = 95.24

# Hardcoded list of expenses in INR
expenses_in_inr = [500, 1200, 2500, 750, 3000]

print("Currency Converter: INR to USD")
print("Exchange Rate: 1 USD = 95.24 INR")
print()

for expense in expenses_in_inr:
    converted_amount = expense / exchange_rate

    print("Original amount:", expense, "INR")
    print("Converted amount:", round(converted_amount, 2), "USD")
    print()
