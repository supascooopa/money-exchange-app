import os
import requests


def currency_converter(from_currency: str, to_currency: str, currency_amount: str):
    url = "https://api.apilayer.com/fixer/convert"
    api_key = os.getenv("api-key")
    payload = {"from": from_currency, "to": to_currency, "amount": currency_amount}
    headers = {"apikey": api_key, }
    response = requests.request("GET", url, headers=headers, params=payload)
    result = response.json()
    return str(result["result"]) + " " + from_currency



