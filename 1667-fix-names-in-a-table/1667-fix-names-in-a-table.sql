SELECT user_id, CONCAT(UPPER(LEFT(name,1)), SUBSTRING(LOWER(name), 2, LENGTH(name))) as name
FROM Users
ORDER BY user_id