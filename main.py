import argparse
from src.converter import CurrencyConverter
from src.logger import setup_logger


def main():
    logger = setup_logger()

    parser = argparse.ArgumentParser(
        description="Currency Converter"
    )

    parser.add_argument(
        "--from",
        dest="from_currency",
        required=True,
        help="Source currency code, e.g. USD"
    )

    parser.add_argument(
        "--to",
        dest="to_currency",
        required=True,
        help="Target currency code, e.g. EUR"
    )

    parser.add_argument(
        "--amount",
        required=True,
        type=float,
        help="Amount to convert"
    )

    args = parser.parse_args()

    try:
        converter = CurrencyConverter("rates.json")

        result = converter.convert(
            args.from_currency,
            args.to_currency,
            args.amount
        )

        print(
            f"{args.amount:.2f} {args.from_currency.upper()} = "
            f"{result:.2f} {args.to_currency.upper()}"
        )

        logger.info(
            f"Conversion successful: {args.amount} "
            f"{args.from_currency.upper()} to "
            f"{args.to_currency.upper()} = {result:.2f}"
        )

    except ValueError as error:
        print(f"Error: {error}")
        logger.error(str(error))

    except FileNotFoundError:
        print("Error: rates.json file was not found.")
        logger.error("rates.json file was not found.")

    except Exception as error:
        print("Error: Something went wrong. Please try again.")
        logger.error(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()