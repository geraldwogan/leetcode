SELECT name, IFNULL(SUM(distance), 0) as travelled_distance
FROM Users u
LEFT JOIN Rides r ON r.user_id = u.id
GROUP BY u.id
ORDER BY travelled_distance desc, name asc