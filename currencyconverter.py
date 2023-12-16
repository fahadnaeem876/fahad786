import os
from flask import Flask, render_template, request, jsonify ,Blueprint
import requests

currencyconverter_app = Blueprint("currencyconerter",__name__)

class CurrencyConverter:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://open.er-api.com/v6/latest/"

    def get_exchange_rates(self, base_currency):
        url = f"{self.base_url}{base_currency}"
        params = {"apikey": self.api_key}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            rates = data.get("rates")
            return rates
        else:
            return None

    def convert_currency(self, amount, from_currency, to_currency):
        rates = self.get_exchange_rates(from_currency)

        if rates:
            if to_currency in rates:
                converted_amount = amount * rates[to_currency]
                return converted_amount
            else:
                return None

@currencyconverter_app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        api_key =os.environ.get("currency_api_key")
        converter = CurrencyConverter(api_key)

        amount = float(request.form.get("amount"))
        from_currency = request.form.get("from_currency").upper()
        to_currency = request.form.get("to_currency").upper()

        converted_amount = converter.convert_currency(amount, from_currency, to_currency)

        if converted_amount is not None:
            return render_template("currencyconverter.html", result=f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

    return render_template("currencyconverter.html", result=None)
