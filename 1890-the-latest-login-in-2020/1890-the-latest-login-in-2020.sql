SELECT user_id, MAX(time_stamp) as  last_stamp
FROM Logins
WHERE time_stamp >= '2020-01-01 00:00:00' and time_stamp < '2021-01-01 00:00:00'
GROUP By user_id