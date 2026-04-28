Query Clauses

SELECT -> Determines which colums to include in the query's result set
FROM -> Identifies the tables
WHERE -> Restricts the number of rows in the final result set
GROUP BY -> Used to group rows together by commin column values
HAVING -> Restricts the number of rows in the final result
ORDER BY -> Sorts the rows of the final result set by one or more columns



The ORDER BY clause: it is a mechanism for sorting result set usinf either raw column data or expressions based on column data.



SELECT fname, lname FROM person WHERE country NOT IN ('USA', 'Canada', NULL);

This query will return nothing, because if we include NULL in NOT IN operations, SQL will every value as !=


RULE: WHEN QUERY HAS AND and OR -> Always parenthise! -> Beauliu CH.4!


De Morgan's LAW


Always pair LIMIT with ORDER BY!

OFFSET = (page - 1) * page_size. Page 2 with size 5 → OFFSET 5.


ORDER BY state IS NULL, state;
-- IS NULL returns 0 (false) or 1 (true). 0s come first → non-nulls first.


Why LIMIT 10 OFFSET 1000000 is slow on large table?

Coz DB should check for every value in database


KeySet pagination -> Cursor pagination

```

SELECT * FROM person 
WHERE person_id > 1000000 
ORDER BY person_id
LIMIT 10;

```

If we want to make case sensitive in LIKE operation, we should write LIKE BINARY "%a", 
by default LIKE is not case sensitive

