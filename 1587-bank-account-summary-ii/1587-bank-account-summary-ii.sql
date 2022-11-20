SELECT name as NAME, SUM(amount) as BALANCE
FROM Users u
LEFT JOIN Transactions t ON u.account = t.account
GROUP BY u.account
HAVING BALANCE > 10000