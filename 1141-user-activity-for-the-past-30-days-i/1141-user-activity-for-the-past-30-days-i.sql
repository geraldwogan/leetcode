SELECT activity_date as day, COUNT(DISTINCT user_id) as active_users
FROM Activity
# WHERE activity_date is not null
# WHERE active_users != 0
WHERE activity_date BETWEEN CAST('2019-07-28' AS DATE) - INTERVAL 30 DAY AND CAST('2019-07-28' AS DATE) 

GROUP BY activity_date

