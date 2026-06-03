# 1...........................................

# class Kitob:
#     def __init__(self,nomi,muallifi,narxi,nashriyoti):
#         self.nom = nomi
#         self.muallif = muallifi
#         self.narx = narxi
#         self.nashriyot = nashriyoti

#     def chiqarish(self):
#         print(f"Nomi: {self.nom}")
#         print(f"Muallif: {self.muallif}")
#         print(f"Narx: {self.narx}")
#         print(f"Nashriyot: {self.nashriyot}")
    
# k1 = Kitob("Kitob 1", "Ali", 50000, "Anor")
# k2 = Kitob("Kitob 2", "Vali", 60000, "Hilol")
# k3 = Kitob("Kitob 3", "Samir", 55000, "Ziyo")
# k4 = Kitob("Kitob 4", "Karim", 30000, "Humo")
# k5 = Kitob("Kitob 5", "Aziz", 45000, "Hilol")

# kitoblar = [k1,k2,k3,k4,k5]
# for kitob in kitoblar:
#     if kitob.nashriyot[0].upper() in "ABCDEFGH":
#         kitob.chiqarish()


# 2................................................

# class Computer:
#     def __init__(self,nom,ram,narx,protsessor):
#         self.nom = nom
#         self.ram = ram
#         self.narx = narx
#         self.protsessor = protsessor

#     def chiqarish(self):
#         print(f'''
# Nomi: {self.nom}
# Rami:{self.ram}
# Narxi: {self.narx}
# Protsessori: {self.protsessor}''')

# k1 = Computer("HP", 8, 700, "i5")
# k2 = Computer("Dell", 16, 900, "i7")
# k3 = Computer("Lenovo", 12, 800, "Ryzen 5")
# k4 = Computer("Asus", 32, 1200, "i9")

# comp = [k1,k2,k3,k4]
# for i in comp:
#     if 4 < i.ram <16:
#         i.chiqarish()


# 3............................................

class User:
    def __init__(self,ism,username,email):
        self.name = ism
        self.username = username
        self.email = email

    def change_username(self, new_username):
        self.username = new_username

    def get_info(self):
        print(f'''Ism: {self.name}
Username: {self.username}
Email: {self.email}''')
        
u1 = User("Aziz Azimoz","aziZ1","azizazimov13@gmail.com")
u2 = User("Ali Sheraliyev","aliSher001","alisherali@gmail.com")
u3 = User("Askerova Samira","sam1ra","askerova.sm@gmail.com")

u1.get_info()
u2.get_info()
u3.get_info()

u1.change_username("Azimov01")
u1.get_info()