create database foundation198;
create table computer(
    brand TEXT,
    model TEXT,
    cpu text,
    frequency decimal,
    ram int,
    os text,
    price decimal
);
insert into computer values("Apple","MacBook Pro14","Apple M5 Pro",4.5, 24, "macOS",1699),
                           ("Samsung","Galaxy Book5 Pro","Intel Core Ultra7", 4.8, 16, "Windows 11 Home", 1400),
                           ("ASUS", "Vivobook 15", "Intel Core i5", 4.5, 8, "Windows 11", 800),
                           ("HP", "HP Pavilion 15", "Intel Core i5-1335U", 4.6, 16, "Windows 11 Home", 700),
                           ("Dell","XPS 13","Intel Core i7-1360P",5.0,16,"Windows 11 Pro",1200),
                           ("Dell","Inspiron 15","Intel Core i5-1235U",4.4,8,"Windows 11 Home",650),
                           ("Lenovo","ThinkPad X1 Carbon","Intel Core i7-1370P",5.0,32,"Windows 11 Pro",1800),
                           ("Lenovo","IdeaPad Slim 5","AMD Ryzen 7 8845HS",4.9,16,"Windows 11 Home",950),
                           ("Acer","Aspire 5","Intel Core i5-13420H",4.6,16,"Windows 11 Home",750),
                           ("Acer","Nitro V 15","AMD Ryzen 7 7735HS",4.8,16,"Windows 11 Home",1100),
                           ("MSI","Katana 15","Intel Core i7-13620H",4.9,16,"Windows 11 Home",1300),
                           ("MSI","Modern 14","Intel Core i5-1335U",4.6,8,"Windows 11 Home",700),
                           ("Huawei","MateBook D16","Intel Core i9-13900H",5.0,16,"Windows 11 Home",1400),
                           ("Huawei","MateBook X Pro","Intel Core Ultra 7",4.8,32,"Windows 11 Pro",2000),
                           ("Apple","MacBook Air M3","Apple M3",4.1,16,"macOS",1299),
                           ("Apple","MacBook Pro 16","Apple M4 Max",4.7,36,"macOS",3000),
                           ("ASUS","ROG Zephyrus G16","AMD Ryzen 9 8945HS",5.0,32,"Windows 11 Pro",2200),
                           ("ASUS", "ZenBook 14", "Intel Core i7", 4.8, 8, "Windows 11", 1000),
                           ("Samsung","Galaxy Book4 Edge","Snapdragon X Elite",4.3,16,"Windows 11 Home",1350),
                           ("Samsung","Galaxy Book4 Ultra","Intel Core Ultra 9",5.0,32,"Windows 11 Pro",2400);

mysql> select * from computer;
+---------+--------------------+----------------------+-----------+------+-----------------+-------+
| brand   | model              | cpu                  | frequency | ram  | os              | price |
+---------+--------------------+----------------------+-----------+------+-----------------+-------+
| Apple   | MacBook Pro14      | Apple M5 Pro         |         5 |   24 | macOS           |  1699 |
| Samsung | Galaxy Book5 Pro   | Intel Core Ultra7    |         5 |   16 | Windows 11 Home |  1400 |
| ASUS    | Vivobook 15        | Intel Core i5        |         5 |    8 | Windows 11      |   800 |
| HP      | HP Pavilion 15     | Intel Core i5-1335U  |         5 |   16 | Windows 11 Home |   700 |
| Dell    | XPS 13             | Intel Core i7-1360P  |         5 |   16 | Windows 11 Pro  |  1200 |
| Dell    | Inspiron 15        | Intel Core i5-1235U  |         4 |    8 | Windows 11 Home |   650 |
| Lenovo  | ThinkPad X1 Carbon | Intel Core i7-1370P  |         5 |   32 | Windows 11 Pro  |  1800 |
| Lenovo  | IdeaPad Slim 5     | AMD Ryzen 7 8845HS   |         5 |   16 | Windows 11 Home |   950 |
| Acer    | Aspire 5           | Intel Core i5-13420H |         5 |   16 | Windows 11 Home |   750 |
| Acer    | Nitro V 15         | AMD Ryzen 7 7735HS   |         5 |   16 | Windows 11 Home |  1100 |
| MSI     | Katana 15          | Intel Core i7-13620H |         5 |   16 | Windows 11 Home |  1300 |
| MSI     | Modern 14          | Intel Core i5-1335U  |         5 |    8 | Windows 11 Home |   700 |
| Huawei  | MateBook D16       | Intel Core i9-13900H |         5 |   16 | Windows 11 Home |  1400 |
| Huawei  | MateBook X Pro     | Intel Core Ultra 7   |         5 |   32 | Windows 11 Pro  |  2000 |
| Apple   | MacBook Air M3     | Apple M3             |         4 |   16 | macOS           |  1299 |
| Apple   | MacBook Pro 16     | Apple M4 Max         |         5 |   36 | macOS           |  3000 |
| ASUS    | ROG Zephyrus G16   | AMD Ryzen 9 8945HS   |         5 |   32 | Windows 11 Pro  |  2200 |
| ASUS    | ZenBook 14         | Intel Core i7        |         5 |    8 | Windows 11      |  1000 |
| Samsung | Galaxy Book4 Edge  | Snapdragon X Elite   |         4 |   16 | Windows 11 Home |  1350 |
| Samsung | Galaxy Book4 Ultra | Intel Core Ultra 9   |         5 |   32 | Windows 11 Pro  |  2400 |
+---------+--------------------+----------------------+-----------+------+-----------------+-------+

select * from computer order by price desc limit 1;
+-------+----------------+--------------+-----------+------+-------+-------+
| brand | model          | cpu          | frequency | ram  | os    | price |
+-------+----------------+--------------+-----------+------+-------+-------+
| Apple | MacBook Pro 16 | Apple M4 Max |         5 |   36 | macOS |  3000 |
+-------+----------------+--------------+-----------+------+-------+-------+

select * from computer order by price limit 1;
+-------+-------------+---------------------+-----------+------+-----------------+-------+
| brand | model       | cpu                 | frequency | ram  | os              | price |
+-------+-------------+---------------------+-----------+------+-----------------+-------+
| Dell  | Inspiron 15 | Intel Core i5-1235U |         4 |    8 | Windows 11 Home |   650 |
+-------+-------------+---------------------+-----------+------+-----------------+-------+

select frequency from computer where price between 400 and 1000 and cpu like '%Intel%';
+-----------+
| frequency |
+-----------+
|         5 |
|         5 |
|         5 |
|         5 |
|         4 |
|         5 |
|         5 |
+-----------+

select count(*) from computer where brand = "Apple";
+----------+
| count(*) |
+----------+
|        4 |
+----------+

select * from computer where brand = "ASUS" and os like '%Windows%' and ram = 8 order by price;
+-------+-------------+---------------+-----------+------+------------+-------+
| brand | model       | cpu           | frequency | ram  | os         | price |
+-------+-------------+---------------+-----------+------+------------+-------+
| ASUS  | Vivobook 15 | Intel Core i5 |         5 |    8 | Windows 11 |   800 |
| ASUS  | ZenBook 14  | Intel Core i7 |         5 |    8 | Windows 11 |  1000 |
+-------+-------------+---------------+-----------+------+------------+-------+