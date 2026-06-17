import pymysql

class Mysql:
    def __init__(self):
        self.connectDb()
        self.CREATEdb()
        self.CREATEtb()

    def connectDb(self):
        self.db = pymysql.connect(
            host ='localhost',
            user = 'root',
            password = '1234'
        )
        self.c = self.db.cursor()
    
    def CREATEdb(self):
        self.c.execute('''CREATE database if not exists rest''')
        self.c.execute('''use rest''')

    def CREATEtb(self):
        self.c.execute('''CREATE table IF NOT EXISTS restoranlar(
                       id INT PRIMARY KEY AUTO_INCREMENT,
                       name VARCHAR(50) NOT NULL,
                       address VARCHAR(50) NOT NULL,
                       maxFoodPrice DECIMAL(10,2) NOT NULL,
                       minFoodPrice DECIMAL(10,2) NOT NULL,
                       employeesCount INT NOT NULL,
                       experience INT NOT NULL)''')
        
    def INSERtb(self):
        self.c.execute(f'''INSERT INTO restoranlar(name,address,maxFoodPrice,minFoodPrice,employeesCount,experience)
                            VALUES
                            ('Majbur','Tashkent',120000,30000,25,12),
                            ('Mirvar','Samarkand',150000,35000,30,10),
                            ('Mashhur','Bukhara',180000,40000,40,15),
                            ('Mardor','Andijan',90000,20000,18,8),
                            ('Muborak','Namangan',200000,50000,50,20),
                            ('Rayhon','Tashkent',110000,25000,22,7),
                            ('OshMarkaz','Fergana',130000,28000,28,9),
                            ('Milliy Taomlar','Nukus',170000,45000,35,14),
                            ('Karvon','Jizzakh',140000,32000,26,11),
                            ('Mehror','Khiva',160000,38000,32,13)''')
        self.db.commit()


    def MAXfoodprice(self):
        self.c.execute(f'''SELECT * FROM restoranlar where name LIKE "m%r" ORDER BY maxFoodPrice''')

    def MINfoodprice(self):
        self.c.execute(f'''SELECT name FROM restoranlar ORDER BY minFoodPrice LIMIT 3''')

    def exp(self):
        self.c.execute(f'''SELECT name, maxFoodPrice FROM restoranlar ORDER BY experience DESC LIMIT 4''')

mysql = Mysql()
mysql.INSERtb()
mysql.MAXfoodprice()
mysql.MINfoodprice()
mysql.exp()