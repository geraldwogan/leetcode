# SELECT e.employee_id 
# FROM Employees as e
# JOIN Salaries as s ON e.employee_id = s.employee_id
# WHERE e.name IS NULL
# OR s.salary IS NULL

# SELECT employee_id
# FROM Employees as e
# UNION 
# SELECT employee_id
# FROM Salaries as s
# WHERE s.employee_id IN Employees

SELECT employee_id
FROM Employees
WHERE employee_id NOT IN (SELECT employee_id FROM Salaries)
UNION
SELECT employee_id
FROM Salaries
WHERE employee_id NOT IN (SELECT employee_id FROM Employees)
ORDER BY employee_id