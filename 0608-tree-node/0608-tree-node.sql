SELECT id, 
CASE 
    WHEN p_id is null THEN 'Root'
    WHEN id IN (
        SELECT p_id
        FROM Tree
        WHERE p_id IS NOT NULL
        GROUP BY p_id
        ) THEN 'Inner'
    ELSE 'Leaf'
    END as type
FROM Tree

# INNER Query Result: {"headers": ["p_id"], "values": [[1], [2]]}

# SELECT p_id
# FROM Tree
# WHERE p_id IS NOT NULL
# GROUP BY p_id