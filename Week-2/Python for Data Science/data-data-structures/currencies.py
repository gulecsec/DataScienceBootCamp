# pylint: disable=missing-docstring

RATES = {"USDEUR": 0.85, "GBPEUR": 1.13, "CHFEUR": 0.86, "EURGBP": 0.885, "EURTRY" : 18.55}

def convert(amount, currency):
    """returns the converted amount in the given currency
    amount is a tuple like (100, "EUR")
    currency is a string
    """
    # 100 EUR to USD IS 100 * 0.85
    currency_name = amount[1] + currency
    if currency_name in RATES:
        return round(RATES[currency_name] * float(amount[0]))
    return None
