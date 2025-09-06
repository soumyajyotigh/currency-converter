# Simple Currency Converter in Python

# Exchange rates relative to 1 USD
exchange_rates = {
    "USD": 1.0,
    "EUR": 0.93,
    "INR": 83.0,
    "GBP": 0.82,
    "JPY": 142.0,
    "AUD": 1.62
}

def convert_currency(amount, from_currency, to_currency):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return "Currency not supported!"
    # Convert amount to USD first, then to target currency
    amount_in_usd = amount / exchange_rates[from_currency]
    converted_amount = amount_in_usd * exchange_rates[to_currency]
    return converted_amount

# User input
amount = float(input("Enter amount: "))
from_currency = input("From currency (USD, EUR, INR, GBP, JPY, AUD): ").upper()
to_currency = input("To currency (USD, EUR, INR, GBP, JPY, AUD): ").upper()

# Conversion
result = convert_currency(amount, from_currency, to_currency)
print(f"{amount} {from_currency} = {result:.2f} {to_currency}")
