# def count_passing_students(grades:list[int],passingGrade:int):
#     count = 0
#     for i in grades:
#         if i >= passingGrade:
#             count +=1
#     return count

# grades = [45, 60, 75, 30, 90]
# passingGrade = 60
# print(count_passing_students(grades,passingGrade))


# ...............................................................

# def end_with_gram(words:list[str]):
#     lst = []
#     for i in words:
#         if i[-4:] == "gram":
#             lst.append(i)
#     return lst

# words = ["telegram", "Instagram", "hello", "program", "diagram", "world"]
# print(end_with_gram(words))


# ............................................................................


class employee:
    def __init__(self,name:str, id:str,hourly_rate:float):
        self.name = name
        self.id = id
        self.working_hours = []
        self.hourly_rate = hourly_rate


    def log_hours(self,hour):
        if 0 < hour <= 24:
            self.working_hours.append(hour)
            return True
        return False

    def total_hours(self):
        return sum(self.working_hours)

    def calculate_salary(self):
        return self.total_hours() * self.hourly_rate

    def reset_hours(self):
        self.working_hours.clear()


employee = employee("Javlon", "E101", hourly_rate=20.0)

print(employee.log_hours(8))   	
print(employee.log_hours(9))   	
print(employee.log_hours(10))  	
print(employee.log_hours(25))  	

print(employee.total_hours())       	
print(employee.calculate_salary())  	

employee.reset_hours()
print(employee.total_hours())       	
print(employee.calculate_salary()) 
