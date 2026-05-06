


## Aggregations





## HAVING is for groups, works after GROUP BY


## WHERE is for rows




SELECT
	publisher_id, 
    COUNT(*) AS book_count
    
FROM book 
GROUP BY publisher_id
HAVING COUNT(*) > 2


Subquery comparison operators: 
IN for membership, 
NOT EXISTS for exclusion (safer than NOT IN due to NULL trap), 
EXISTS for "any related rows?". 
ANY and ALL exist but are usually clearer rewritten with IN, NOT IN, MIN, or MAX. 

The key distinction: IN/ANY/ALL compare a value to a list; 
EXISTS just checks if rows exist at all.



Correlated subqueries reference columns from the outer query, which causes them to run once per outer row (like a nested loop). Test: try running the inner query alone — if it fails because of a missing reference, it's correlated. They're powerful for "for each row, check related rows" but can be slow on large data. JOIN-based rewrites are often faster when the question allows it.