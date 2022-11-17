SELECT sp.name
FROM SalesPerson sp
WHERE sp.name NOT IN (
    SELECT sp.name
    FROM Orders o 
    JOIN Company c ON c.com_id = o.com_id
    JOIN SalesPerson sp  ON o.sales_id = sp.sales_id
    WHERE c.name = 'RED'
)