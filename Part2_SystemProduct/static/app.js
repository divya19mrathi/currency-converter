const currencyMeta = {
    USD: { symbol: "$", flag: "🇺🇸" },
    EUR: { symbol: "€", flag: "🇪🇺" },
    INR: { symbol: "₹", flag: "🇮🇳" },
    GBP: { symbol: "£", flag: "🇬🇧" }
};

const form = document.getElementById("converter-form");
const amountInput = document.getElementById("amount");
const fromSelect = document.getElementById("from-currency");
const toSelect = document.getElementById("to-currency");
const swapButton = document.getElementById("swap-button");
const convertButton = document.getElementById("convert-button");
const resultValue = document.getElementById("result-value");
const resultMeta = document.getElementById("result-meta");
const errorMessage = document.getElementById("error-message");
const fromSymbol = document.getElementById("from-symbol");
const fromFlag = document.getElementById("from-flag");
const toFlag = document.getElementById("to-flag");

function setError(message = "") {
    errorMessage.textContent = message;
}

function updateCurrencyVisuals() {
    const from = fromSelect.value;
    const to = toSelect.value;

    fromSymbol.textContent = currencyMeta[from]?.symbol || from;
    fromFlag.textContent = currencyMeta[from]?.flag || "💱";
    toFlag.textContent = currencyMeta[to]?.flag || "💱";
}

async function loadCurrencies() {
    try {
        const response = await fetch("/api/currencies");
        const currencies = await response.json();

        fromSelect.innerHTML = "";
        toSelect.innerHTML = "";

        currencies.forEach((currency) => {
            const optionFrom = new Option(currency, currency);
            const optionTo = new Option(currency, currency);
            fromSelect.add(optionFrom);
            toSelect.add(optionTo);
        });

        fromSelect.value = currencies.includes("USD") ? "USD" : currencies[0];
        toSelect.value = currencies.includes("INR") ? "INR" : currencies[1] || currencies[0];

        updateCurrencyVisuals();
    } catch {
        setError("Could not load currencies. Please check that the server is running.");
    }
}

async function convertCurrency(event) {
    event.preventDefault();
    setError("");

    const amount = amountInput.value.trim();

    if (amount === "") {
        setError("Please enter an amount.");
        amountInput.focus();
        return;
    }

    if (Number.isNaN(Number(amount))) {
        setError("Amount must be a valid number.");
        amountInput.focus();
        return;
    }

    if (Number(amount) < 0) {
        setError("Amount cannot be negative.");
        amountInput.focus();
        return;
    }

    convertButton.disabled = true;
    convertButton.querySelector("span").textContent = "Converting...";

    try {
        const response = await fetch("/api/convert", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                from: fromSelect.value,
                to: toSelect.value,
                amount: amount
            })
        });

        const data = await response.json();

        if (!response.ok || !data.success) {
            throw new Error(data.error || "Conversion failed.");
        }

        resultValue.textContent =
            `${data.result.toLocaleString(undefined, {
                minimumFractionDigits: 2,
                maximumFractionDigits: 2
            })} ${data.to}`;

        resultMeta.textContent =
            `${Number(data.amount).toLocaleString(undefined, {
                minimumFractionDigits: 2,
                maximumFractionDigits: 2
            })} ${data.from} • Rate: ${data.rate}`;

    } catch (error) {
        setError(error.message);
    } finally {
        convertButton.disabled = false;
        convertButton.querySelector("span").textContent = "Convert currency";
    }
}

swapButton.addEventListener("click", () => {
    const oldFrom = fromSelect.value;
    fromSelect.value = toSelect.value;
    toSelect.value = oldFrom;
    updateCurrencyVisuals();
    setError("");
});

fromSelect.addEventListener("change", updateCurrencyVisuals);
toSelect.addEventListener("change", updateCurrencyVisuals);
form.addEventListener("submit", convertCurrency);

loadCurrencies();
