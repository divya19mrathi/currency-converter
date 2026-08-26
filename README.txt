CURRENCY CONVERTER - PART 2
============================

1. PROJECT DESCRIPTION
----------------------
This is a command-line currency converter written in Python.

The application reads exchange rates dynamically from rates.json
and converts an amount from one supported currency to another.

The application also logs successful conversions and errors
to app.log.


2. REQUIREMENTS
---------------
Python 3.x

No external Python packages are required.


3. PROJECT STRUCTURE
--------------------
src/converter.py
    Contains currency conversion logic.

src/logger.py
    Configures application logging.

main.py
    Provides the command-line interface.

rates.json
    Contains exchange rates.

tests/test_converter.py
    Contains automated unit tests.

app.log
    Stores application operations and errors.


4. USAGE
--------
Run the program using:

python main.py --from USD --to EUR --amount 150


5. EXAMPLES
-----------
Example 1:

python main.py --from USD --to EUR --amount 150

Output:

150.00 USD = 127.50 EUR


Example 2:

python main.py --from USD --to INR --amount 100

Output:

100.00 USD = 9524.00 INR


6. ERROR HANDLING
-----------------
The application handles:

- Negative amounts
- Non-numeric amounts
- Unsupported currency codes
- Unsupported currency conversions
- Missing rates.json file

The application displays user-friendly error messages
instead of raw Python tracebacks.


7. EXCHANGE RATE CONFIGURATION
------------------------------
Exchange rates are stored in rates.json.

The rates can be updated by modifying the JSON configuration
file without changing the Python conversion logic.


8. LOGGING
----------
Application operations and errors are stored in:

app.log


9. TESTING
----------
Run the automated tests using:

python -m unittest discover -s tests

The tests cover successful conversions and failure cases.