SELECT 
	o.order_id, 
    CONCAT(c.fname, " ", c.lname),
    b.title, 
    oi.quantity

FROM `order` as o 
LEFT JOIN customer as c ON o.customer_id = c.customer_id
LEFT JOIN order_item as oi ON oi.order_id = o.order_id
LEFT JOIN book as b ON oi.book_id = b.book_id;



#####


SELECT
	b.title, 
    CONCAT(a.fname, " ", a.lname)


FROM book AS b 
LEFT JOIN book_author as ba ON b.book_id = ba.book_id
INNER JOIN author as a ON a.author_id = ba.author_id


####

SELECT
	b.title, 
    c.name

FROM book_category AS bc
LEFT JOIN book as b ON bc.book_id = b.book_id
LEFT JOIN category as c ON bc.category_id = c.category_id
ORDER BY b.title, c.name

####


SELECT
	b.title,
    a.fname, 
    a.lname,
    p.country
    
FROM book AS b 
LEFT JOIN book_author as ba ON ba.book_id = b.book_id
LEFT JOIN author AS a ON ba.author_id = a.author_id
LEFT JOIN publisher AS p ON p.publisher_id = b.publisher_id
WHERE p.country = "Japan"
ORDER BY p.country


####


SELECT
	b.title, 
    CONCAT(c.fname, " ", c.lname),
    oi.quantity
    
FROM customer AS c 
INNER JOIN `order` AS o ON o.customer_id = c.customer_id
INNER JOIN order_item AS oi ON oi.order_id = o.order_id
INNER JOIN book AS b ON b.book_id = oi.book_id
ORDER BY c.customer_id
   
###

SELECT 
	b.title, 
    GROUP_CONCAT(a.lname ORDER BY a.lname)
    
FROM book AS b 
LEFT JOIN book_author AS ba ON b.book_id = ba.book_id
LEFT JOIN author AS a ON ba.author_id = a.author_id
GROUP BY b.book_id, b.title
ORDER BY b.title


####

SELECT
	b.title, 
    r.review_text, 
    CONCAT(c.fname, " ", c.lname),
    p.name, 
    r.rating
 
FROM review AS r 
LEFT JOIN book AS b ON b.book_id = r.book_id
LEFT JOIN customer AS c ON r.customer_id = c.customer_id
LEFT JOIN publisher AS p ON p.publisher_id = b.publisher_id



#####


SELECT 
	b.title, 
    c.name,
    p.name, 
   	CONCAT(a.fname, " ", a.lname),
    b.price
    
FROM book AS b 
INNER JOIN publisher AS p ON p.publisher_id = b.publisher_id
INNER JOIN book_author AS ba ON b.book_id = ba.author_id
INNER JOIN author AS a ON ba.author_id = a.author_id
INNER JOIN book_category AS bc ON bc.book_id = b.book_id
INNER JOIN category AS c ON bc.category_id = c.category_id
WHERE c.name = "Fiction"
ORDER BY b.price DESC;





#### SELF JOINS

SELECT
	CONCAT(c.fname, " ", c.lname),
    CONCAT(ref.fname, " ", ref.lname)
    
FROM customer AS c 
LEFT JOIN customer AS ref
ON c.referrer_id = ref.customer_id




# Juncton tables, Many-to-many
####

SELECT
	CONCAT(a.fname, " ", a.lname),
    b.title
    
FROM author AS a 
LEFT JOIN book_author AS ba ON ba.author_id = a.author_id
LEFT JOIN book AS b ON b.book_id = ba.book_id