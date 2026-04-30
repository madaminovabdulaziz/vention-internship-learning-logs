SELECT b.title, p.name AS publisher_name
FROM book b
INNER JOIN publisher p ON b.publisher_id = p.publisher_id;


# LEFT JOIN


SELECT b.title, p.name AS publisher_name
FROM book b
LEFT JOIN publisher p ON b.publisher_id = p.publisher_id;




# MULTIPLE INNER JOIN

SELECT b.title, a.fname, a.lname
FROM book AS b
INNER JOIN book_author AS ba ON b.book_id = ba.book_id
INNER JOIN author AS a ON ba.author_id = a.author_id;



# 4 table JOIN
# The question: "Show every order with the customer's name, the book they ordered, and the book's publisher."


SELECT 
    o.order_id, 
    c.fname, 
    b.title, 
    p.name AS publisher

FROM `order` AS o
INNER JOIN customer AS c ON o.customer_id = c.customer_id
INNER JOIN order_item AS oi ON o.order_id = oi.order_id
INNER JOIN book AS b ON b.book_id = oi.book_id
INNER JOIN publisher AS p on b.publisher_id = p.pusblisher_id
ORDER BY order_id;




# The question: Show each book's title and all the categories it belongs to.

SELECT b.title, c.name
FROM book as b
INNER JOIN book_category as bc ON bc.book_id = b.book_id
INNER JOIN category AS c ON c.category_id = bc.category_id;



# SELF JOIN

SELECT 
    c.fname AS customer, 
    c.lname AS customer_last,
    r.fname AS referred_by

FROM customer AS c 
INNER JOIN customer AS r ON c.referred_id = r.customer_id
ORDER BY c.customer_id





# CROSS JOIN

# NOTE: this is what causes Cartesian product!
