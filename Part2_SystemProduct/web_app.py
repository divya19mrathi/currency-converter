from pathlib import Path

from flask import Flask, jsonify, render_template, request

from src.converter import CurrencyConverter
from src.logger import setup_logger


BASE_DIR = Path(__file__).resolve().parent
RATES_FILE = BASE_DIR / "rates.json"

app = Flask(__name__)

logger = setup_logger()

converter = CurrencyConverter(RATES_FILE)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/currencies")
def currencies():
    return jsonify(sorted(converter.rates.keys()))


@app.route("/api/convert", methods=["POST"])
def convert():

    try:
        data = request.get_json(silent=True) or {}

        from_currency = str(
            data.get("from", "")
        ).strip().upper()

        to_currency = str(
            data.get("to", "")
        ).strip().upper()

        raw_amount = data.get("amount")

        if not from_currency or not to_currency:
            raise ValueError(
                "Please select both currencies."
            )

        if raw_amount is None or str(raw_amount).strip() == "":
            raise ValueError(
                "Please enter an amount."
            )

        try:
            amount = float(raw_amount)

        except (TypeError, ValueError):
            raise ValueError(
                "Amount must be a valid number."
            )

        if amount < 0:
            raise ValueError(
                "Amount cannot be negative."
            )

        result = converter.convert(
            from_currency,
            to_currency,
            amount
        )

        if from_currency == to_currency:
            rate = 1.0

        else:
            rate = converter.rates[
                from_currency
            ][to_currency]

        logger.info(
            "Web conversion successful: %.2f %s to %s = %.2f",
            amount,
            from_currency,
            to_currency,
            result
        )

        return jsonify({
            "success": True,
            "from": from_currency,
            "to": to_currency,
            "amount": amount,
            "result": result,
            "rate": rate
        })

    except ValueError as error:

        logger.error(
            "Web conversion error: %s",
            error
        )

        return jsonify({
            "success": False,
            "error": str(error)
        }), 400

    except Exception as error:

        logger.exception(
            "Unexpected web application error"
        )

        return jsonify({
            "success": False,
            "error": (
                "Something went wrong. "
                "Please try again."
            )
        }), 500


if __name__ == "__main__":
    app.run(debug=True)