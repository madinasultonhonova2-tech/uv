CREATE TABLE genre(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50) NOT NULL);

CREATE TABLE author(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50) NOT NULL);

CREATE TABLE book(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    price INT,
    amount INT,
    g_id INT,
    a_id INT,
    FOREIGN KEY (g_id) REFERENCES genre(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (a_id) REFERENCES author(id) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO genre(name) VALUES("Roman"), ("Fantastika"), ("Dramma"), ("Tragediya");

INSERT INTO author(name) VALUES("Alisher Navoiy"), ("Pushkin"), ("Bobur"), ("Abdulla Qodiriy");

INSERT INTO book
    (name, price, amount, g_id, a_id) 
VALUES
    ("O'tgan kunlar", 35000, 10, 4, 1),
    ("Shaytanant", 15000, 5, 1, 3),
    ("Hamsa", 150000, 1, 2, 1),
    ("Odam bo'lish qiyin", 10000, 20, 2, 2),
    ("Diqqat", 17000, 2, 3, 4),
    ("12 yil qullikda", 10000, 2, 1, 2),
    ("Jinoyat va jazo", 17000, 8, 4, 1),
    ("Oq kechalar", 25000, 2, 3, 3),
    ("Atom Odatlar", 35000, 3, 2, 4),
    ("Yulduzli tunlar", 39000, 1, 1, 1),
    ("Dunyoning ishlari", 31000, 4, 2, 3),
    ("Kichik Shahzoda", 1000, 5, 1, 2),
    ("Kecha va Kunduz", 19000, 10, 4, 4),
    ("Bilmasvoy", 17000, 5, 2, 1);
    

SELECT * FROM book AS b
JOIN author AS a 
ON b.a_id = a.id;
+----+--------------------+--------+--------+------+------+----+-----------------+
| id | name               | price  | amount | g_id | a_id | id | name            | 
+----+--------------------+--------+--------+------+------+----+-----------------+
|  1 | O'tgan kunlar      |  35000 |     10 |    4 |    1 |  1 | Alisher Navoiy  |
|  3 | Hamsa              | 150000 |      1 |    2 |    1 |  1 | Alisher Navoiy  |
|  7 | Jinoyat va jazo    |  17000 |      8 |    4 |    1 |  1 | Alisher Navoiy  |
| 10 | Yulduzli tunlar    |  39000 |      1 |    1 |    1 |  1 | Alisher Navoiy  |
| 14 | Bilmasvoy          |  17000 |      5 |    2 |    1 |  1 | Alisher Navoiy  |
|  4 | Odam bo'lish qiyin |  10000 |     20 |    2 |    2 |  2 | Pushkin         |
|  6 | 12 yil qullikda    |  10000 |      2 |    1 |    2 |  2 | Pushkin         |
| 12 | Kichik Shahzoda    |   1000 |      5 |    1 |    2 |  2 | Pushkin         |
|  2 | Shaytanant         |  15000 |      5 |    1 |    3 |  3 | Bobur           |
|  8 | Oq kechalar        |  25000 |      2 |    3 |    3 |  3 | Bobur           |
| 11 | Dunyoning ishlari  |  31000 |      4 |    2 |    3 |  3 | Bobur           |
|  5 | Diqqat             |  17000 |      2 |    3 |    4 |  4 | Abdulla Qodiriy |
|  9 | Atom Odatlar       |  35000 |      3 |    2 |    4 |  4 | Abdulla Qodiriy |
| 13 | Kecha va Kunduz    |  19000 |     10 |    4 |    4 |  4 | Abdulla Qodiriy |
+----+--------------------+--------+--------+------+------+----+-----------------+



SELECT * FROM book AS b
JOIN author AS a 
ON b.a_id = a.id
WHERE a.id = 1;
+----+-----------------+--------+--------+------+------+----+----------------+
| id | name            | price  | amount | g_id | a_id | id | name           |
+----+-----------------+--------+--------+------+------+----+----------------+
|  1 | Otgan kunlar    |  35000 |     10 |    4 |    1 |  1 | Alisher Navoiy |
|  3 | Hamsa           | 150000 |      1 |    2 |    1 |  1 | Alisher Navoiy |
|  7 | Jinoyat va jazo |  17000 |      8 |    4 |    1 |  1 | Alisher Navoiy |
| 10 | Yulduzli tunlar |  39000 |      1 |    1 |    1 |  1 | Alisher Navoiy |
| 14 | Bilmasvoy       |  17000 |      5 |    2 |    1 |  1 | Alisher Navoiy |
+----+-----------------+--------+--------+------+------+----+----------------+


SELECT * FROM book AS b
JOIN author AS a
ON a.id = b.a_id
JOIN genre AS g 
ON g.id = b.g_id;
+----+--------------------+--------+--------+------+------+----+-----------------+----+------------+
| id | name               | price  | amount | g_id | a_id | id | name            | id | name       |
+----+--------------------+--------+--------+------+------+----+-----------------+----+------------+
|  1 | O'tgan kunlar      |  35000 |     10 |    4 |    1 |  1 | Alisher Navoiy  |  4 | Tragediya  |
|  3 | Hamsa              | 150000 |      1 |    2 |    1 |  1 | Alisher Navoiy  |  2 | Fantastika |
|  7 | Jinoyat va jazo    |  17000 |      8 |    4 |    1 |  1 | Alisher Navoiy  |  4 | Tragediya  |
| 10 | Yulduzli tunlar    |  39000 |      1 |    1 |    1 |  1 | Alisher Navoiy  |  1 | Roman      |
| 14 | Bilmasvoy          |  17000 |      5 |    2 |    1 |  1 | Alisher Navoiy  |  2 | Fantastika |
|  4 | Odam bo'lish qiyin |  10000 |     20 |    2 |    2 |  2 | Pushkin         |  2 | Fantastika |
|  6 | 12 yil qullikda    |  10000 |      2 |    1 |    2 |  2 | Pushkin         |  1 | Roman      |
| 12 | Kichik Shahzoda    |   1000 |      5 |    1 |    2 |  2 | Pushkin         |  1 | Roman      |
|  2 | Shaytanant         |  15000 |      5 |    1 |    3 |  3 | Bobur           |  1 | Roman      |
|  8 | Oq kechalar        |  25000 |      2 |    3 |    3 |  3 | Bobur           |  3 | Dramma     |
| 11 | Dunyoning ishlari  |  31000 |      4 |    2 |    3 |  3 | Bobur           |  2 | Fantastika |
|  5 | Diqqat             |  17000 |      2 |    3 |    4 |  4 | Abdulla Qodiriy |  3 | Dramma     |
|  9 | Atom Odatlar       |  35000 |      3 |    2 |    4 |  4 | Abdulla Qodiriy |  2 | Fantastika |
| 13 | Kecha va Kunduz    |  19000 |     10 |    4 |    4 |  4 | Abdulla Qodiriy |  4 | Tragediya  |
+----+--------------------+--------+--------+------+------+----+-----------------+----+------------+


SELECT 
    a_id, a.name, JSON_ARRAYAGG(b.name) AS books, JSON_ARRAYAGG(g.name) As genres 
FROM 
    book AS b
JOIN 
    author AS a ON a.id = b.a_id
JOIN 
    genre AS g ON g.id = b.g_id
GROUP BY 
    a_id;
+------+-----------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------+
| a_id | name            | books                                                                         | genres                                                          |
+------+-----------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------+
|    1 | Alisher Navoiy  | ["O'tgan kunlar", "Hamsa", "Jinoyat va jazo", "Yulduzli tunlar", "Bilmasvoy"] | ["Tragediya", "Fantastika", "Tragediya", "Roman", "Fantastika"] |
|    2 | Pushkin         | ["Odam bo'lish qiyin", "12 yil qullikda", "Kichik Shahzoda"]                  | ["Fantastika", "Roman", "Roman"]                                |
|    3 | Bobur           | ["Shaytanant", "Oq kechalar", "Dunyoning ishlari"]                            | ["Roman", "Dramma", "Fantastika"]                               |
|    4 | Abdulla Qodiriy | ["Diqqat", "Atom Odatlar", "Kecha va Kunduz"]                                 | ["Dramma", "Fantastika", "Tragediya"]                           |
+------+-----------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------+


SELECT DISTINCT g.name
FROM book b
JOIN author a ON b.a_id = a.id
JOIN genre g ON b.g_id = g.id
WHERE a.name = 'Alisher Navoiy';
+------------+
| name       |
+------------+
| Roman      |
| Fantastika |
| Tragediya  |
+------------+

SELECT a.name,
       GROUP_CONCAT(DISTINCT g.name) AS genres
FROM book b
JOIN author a ON b.a_id = a.id
JOIN genre g ON b.g_id = g.id
GROUP BY a.id, a.name;
+-----------------+-----------------------------+
| name            | genres                      |
+-----------------+-----------------------------+
| Alisher Navoiy  | Fantastika,Roman,Tragediya  |
| Pushkin         | Fantastika,Roman            |
| Bobur           | Dramma,Fantastika,Roman     |
| Abdulla Qodiriy | Dramma,Fantastika,Tragediya |
+-----------------+-----------------------------+

SELECT g.name, COUNT(*) as soni
FROM book b
JOIN genre g on b.g_id = g.id
GROUP BY g.id, g.name
ORDER BY soni DESC
LIMIT 1;
+------------+------+
| name       | soni |
+------------+------+
| Fantastika |    5 |
+------------+------+

SELECT a.name as a, g.name as g, COUNT(*) AS kitob_soni
FROM book b
JOIN author a ON b.a_id = a.id
JOIN genre g ON b.g_id = g.id
GROUP BY a.name, g.name;
+-----------------+------------+-------------+
| author          | genre      | books_count |
+-----------------+------------+-------------+
| Alisher Navoiy  | Tragediya  |           2 |
| Alisher Navoiy  | Fantastika |           2 |
| Alisher Navoiy  | Roman      |           1 |
| Pushkin         | Fantastika |           1 |
| Pushkin         | Roman      |           2 |
| Bobur           | Roman      |           1 |
| Bobur           | Dramma     |           1 |
| Bobur           | Fantastika |           1 |
| Abdulla Qodiriy | Dramma     |           1 |
| Abdulla Qodiriy | Fantastika |           1 |
| Abdulla Qodiriy | Tragediya  |           1 |
+-----------------+------------+-------------+

-- SELECT a.name as a, g.name as g, COUNT(*) AS kitob_soni
-- FROM book b
-- JOIN author a ON b.a_id = a.id
-- JOIN genre g ON b.g_id = g.id
-- GROUP BY a.name, g.name
-- ORDER BY kitob_soni desc
-- LIMIT 1;


SELECT a.name, SUM(b.amount) AS jami_sotilgan
FROM book b
JOIN author a ON b.a_id = a.id
GROUP BY a.id, a.name
ORDER BY jami_sotilgan DESC
LIMIT 1;

+---------+---------------+
| name    | jami_sotilgan |
+---------+---------------+
| Pushkin |            27 |
+---------+---------------+