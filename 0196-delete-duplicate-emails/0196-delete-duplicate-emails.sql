DELETE 
FROM Person
WHERE ID NOT IN
(
    SELECT * 
    FROM
    (
        SELECT MIN(id)
        FROM Person
        GROUP BY email
    ) as temp_person
)