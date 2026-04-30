# RULE 1: Never cause Cartesian Product! It will kill performance!
# RULE 2: When choosing between INNER/LEFT JOIN ask: What should happen to rows that don't have match?
# -> Drop them silently -> INNER JOIN
# -> Keep them with NULL -> LEFT JOIN

# RULE 3: NULL is not equal to NULL in databases! Never compare them!



# Foreign key = > a column that references another table's primary key




When doing JOIN, SQL by default is doing INNER JOIN

So doing JOIN alone, means -> INNER JOIN

That's why INNER is optional in this case

But it is a good practice to do write and specify what type of join I am doing.
EX:

```
SELECT b.title, p.name AS publisher_name 
FROM book b
INNER JOIN publishe p ON b.publisher_id = p.publisher_id;

```




SO what is INNER JOIN?

INNER JOIN is way to get data from 2 or more tables, related to each other, usually by some ID's,
in our casse is publisher_id, but the way we get is interesting.

INNER JOIN drops rows if it can't find matching ID's. So INNER JOIN exclusively fetches 
only rows matching on both sides.

So it basically says: only keep rows where I found matches in both tables


Now let's talk about LEFT JOIN's

So left join is returning values matching on the right table, if not matching exists,
returns NULL basically. For example, in INNER JOIN, even we have data on LEFT table but it does
not match RIGHT table, this rows silently dropped, only values in BOTH tables are taken.

But, in LEFT JOIN, is, all rows are taken, whether matching rows exist in RIGHT table. If yes = return value
If not -> return NULL







-------------------




Now, let's talk about Multiple table JOIN's

So when we need them?

When or DB query has:
# 1. Query from more than 2 tables
# 2. When we have Many-to-Many relationships
# 3. Because, when we have MTM relationship, we have a separate table wich records it

Example:
One book can have multiple authors <-> one author can have multiple books etc

