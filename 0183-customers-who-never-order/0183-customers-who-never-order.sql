SELECT Customers.name as "Customers"
FROM Orders
RIGHT JOIN Customers ON Customers.id = Orders.customerId
WHERE Orders.id IS NULL