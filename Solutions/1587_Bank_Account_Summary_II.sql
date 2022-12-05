SELECT
    u.name,
    SUM(t.amount) AS balance
FROM Users u
LEFT JOIN Transactions t on u.account = t.account
GROUP BY u.account
HAVING SUM(t.amount) > 10000
