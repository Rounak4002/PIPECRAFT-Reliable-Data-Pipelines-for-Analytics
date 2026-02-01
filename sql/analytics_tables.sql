CREATE TABLE currency_summary AS
SELECT
    base_currency,
    COUNT(currency) AS total_currencies,
    AVG(rate) AS average_rate
FROM exchange_rates
GROUP BY base_currency;

SELECT * FROM currency_summary;
