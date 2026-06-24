# 1....................................

# class Playlist:
#     def __init__(self,owner:str):
#         self.owner = owner
#         self.tracks = []

#     def add_track(self,title,artist):
#         self.tracks.append((title, artist))

#     def remove_last(self):
#         if self.tracks:
#             return self.tracks.pop()

#     def total_tracks(self):
#         return len(self.tracks)

#     def unique_tracks(self):
#         lst = []
#         for i in self.tracks:
#             if self.tracks not in lst:
#                 lst.append(i)
#         return lst
    
#     def search_by_title(self,title:str):
#         lst = []
#         for i in self.tracks:
#             if i[0] == title:
#                 lst.append(i)
#         return lst

#     def filter_by_artist(self,artist:str):
#         result = []
#         for i in self.tracks:
#             if i[1] == artist:
#                 result.append(i)
#         return result


# pl= Playlist("Muhammad")

# pl.add_track("Yomg'irlar", "Shahzoda")
# pl.add_track("Gulim", "Yulduz Usmonova")
# pl.add_track("Yomg'irlar", "Shahzoda")
# pl.add_track("Xayr edi", "Lola")
# pl.add_track("Kel", "Ulug'bek Rahmatullayev")

# print(pl.total_tracks())
# print(pl.filter_by_artist("Shahzoda"))
# print(pl.remove_last())
# print(pl.search_by_title("Kel"))
# print(pl.unique_tracks())


# 2................................................

# class Employee:
#     def __init__(self,name:str,id:str,hourly_rate:float):
#         self.name = name
#         self.id = id
#         self.hourly_rate = hourly_rate
#         self.working_hours = []

#     def log_hours(self,hour:int):
#         if 0 < hour <= 24:
#             self.working_hours.append(hour)
#             return True
#         return False
        
#     def total_hours(self):
#         return sum(self.working_hours)
    
#     def calculate_salary(self):
#         return self.total_hours() * self.hourly_rate

#     def reset_hours(self):
#         self.working_hours.clear()

# employee = Employee("Javlon", "E101", hourly_rate=20.0)

# print(employee.log_hours(8))   	
# print(employee.log_hours(9))   	
# print(employee.log_hours(10))  	
# print(employee.log_hours(25))  	

# print(employee.total_hours())       	
# print(employee.calculate_salary())  	

# employee.reset_hours()
# print(employee.total_hours())       
# print(employee.calculate_salary())  	


# 3..............................................

class Student:
    def __init__(self,name:str,id:str):
        self.name = name
        self.id  = id
        self.grades = []

    def add_grade(self,grade:int):
        self.grades.append(grade)
    

    def calculate_average(self):
        return sum(self.grades) / len(self.grades)

    def get_status(self):
        avg = self.calculate_average
        if 90 <= avg <= 100:
            return "A'lo"
        elif 80 <= avg < 90:
            return "Yaxshi"
        elif 70 <= avg < 80:
            return "Qoniqarli"
        else:
            return "Qoniqarsiz"

student = Student("Nodira", "S123")
student.add_grade(85)
student.add_grade(90)
 
print(student.calculate_average())
print(student.get_status())