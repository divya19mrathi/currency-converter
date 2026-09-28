CURRENCY CONVERTER - PART 2
============================

1. PROJECT DESCRIPTION
----------------------
This is a Python currency converter with both:
- A command-line interface (CLI)
- A browser-based graphical user interface (GUI)

The application reads exchange rates dynamically from rates.json.
The web interface is served by Flask and uses the same CurrencyConverter
class as the CLI, so there is one conversion logic source.

Successful operations and errors are logged to app.log.


2. REQUIREMENTS
---------------
Python 3.x
Flask 3.x

Install the dependency with:

pip install -r requirements.txt


3. PROJECT STRUCTURE
--------------------
main.py
    Command-line interface.

web_app.py
    Flask web application and API endpoints.

src/converter.py
    Currency conversion logic.

src/logger.py
    Logging configuration.

templates/index.html
    Web interface.

static/style.css
    UI styling and responsive layout.

static/app.js
    Browser-side interaction.

rates.json
    Exchange-rate configuration.

test/test_converter.py
    Automated unit tests.

app.log
    Application operation and error log.


4. RUN THE WEB INTERFACE
------------------------
Open a terminal in this folder:

Part2_SystemProduct

Install dependencies:

pip install -r requirements.txt

Start the web application:

python web_app.py

Then open this address in your browser:

http://127.0.0.1:5000


5. USING THE WEB INTERFACE
--------------------------
1. Enter an amount.
2. Select the source currency.
3. Select the target currency.
4. Click "Convert currency".
5. Use the swap button (⇄) to switch currencies.


6. CLI USAGE
------------
The original command-line interface is still available.

Example:

python main.py --from USD --to EUR --amount 150

Example output:

150.00 USD = 127.50 EUR


7. EXAMPLES
-----------
Example 1:

python main.py --from USD --to EUR --amount 150

Output:

150.00 USD = 127.50 EUR


Example 2:

python main.py --from USD --to INR --amount 100

Output:

100.00 USD = 9524.00 INR


8. ERROR HANDLING
-----------------
The application handles:
- Negative amounts
- Non-numeric amounts
- Unsupported currency codes
- Unsupported currency conversions
- Missing rates.json
- Missing or invalid web input

The web interface displays friendly error messages instead of raw
Python tracebacks.


9. EXCHANGE RATE CONFIGURATION
------------------------------
Exchange rates are stored in rates.json.

They can be updated by modifying the JSON configuration file without
changing the conversion logic.


10. LOGGING
-----------
Operations and errors are stored in:

app.log


11. TESTING
-----------
Run the automated tests with:

python -m unittest discover -s test

The tests cover successful conversions and failure cases.


12. GITHUB
----------
Commit the project after testing:

git add .
git commit -m "Add currency converter web interface"
git push

Do not commit Python cache folders such as __pycache__.
