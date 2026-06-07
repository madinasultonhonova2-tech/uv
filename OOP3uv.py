class MyDate:
    MONTHS = [
        "Yanvar", "Fevral", "Mart", "Aprel",
        "May", "Iyun", "Iyul", "Avgust",
        "Sentabr", "Oktabr", "Noyabr", "Dekabr"
    ]

    def __init__(self,day,month,year):
        if not self.isValidDate(day, month, year):
            raise ValueError("Noto'g'ri sana!")
        self.day = day
        self.month = month
        self.year = year

    def isLeapYear(self, year):
        return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

    def getDaysInMonth(self, month, year):
        days = [31, 28, 31, 30, 31, 30,
                31, 31, 30, 31, 30, 31]

        if month == 2 and self.isLeapYear(year):
            return 29

        return days[month - 1]

    def isValidDate(self, day, month, year):
        if not (1 <= year <= 9999):
            return False

        if not (1 <= month <= 12):
            return False
    
        max_day = self.getDaysInMonth(month, year)

        if not (1 <= day <= max_day):
            return False
        return True

    def setDate(self, day, month, year):
        if not self.isValidDate(day, month, year):
            raise ValueError("Noto'g'ri sana!")

        self.day = day
        self.month = month
        self.year = year

    def nextDay(self):
        max_day = self.getDaysInMonth(self.month, self.year)

        if self.day < max_day:
            self.day += 1
        else:
            self.day = 1

            if self.month < 12:
                self.month += 1
            else:
                self.month = 1
                self.year += 1

        return self

    def previousDay(self):
        if self.day > 1:
            self.day -= 1
        else:
            if self.month > 1:
                self.month -= 1
            else:
                self.month = 12
                self.year -= 1

            self.day = self.getDaysInMonth(
                self.month,
                self.year
            )

        return self

    def nextMonth(self):
        if self.month == 12:
            self.month = 1
            self.year += 1
        else:
            self.month += 1

        max_day = self.getDaysInMonth(self.month, self.year)
        if self.day > max_day:
            self.day = max_day

        return self

    def previousMonth(self):
        if self.month == 1:
            self.month = 12
            self.year -= 1
        else:
            self.month -= 1

        max_day = self.getDaysInMonth(self.month, self.year)
        if self.day > max_day:
            self.day = max_day

        return self

    def nextYear(self):
        new_year = self.year + 1

        if not self.isValidDate(
            self.day,
            self.month,
            new_year
        ):
            self.day = 28

        self.year = new_year
        return self

    def previousYear(self):
        new_year = self.year - 1

        if new_year < 1:
            raise ValueError("Yil 1 dan kichik bo'lishi mumkin emas!")

        if not self.isValidDate(
            self.day,
            self.month,
            new_year
        ):
            self.__day = 28

        self.year = new_year
        return self

    def __str__(self):
        return f"{self.day}-{self.MONTHS[self.month - 1]} {self.year} yil"


d = MyDate(28, 2, 2024)

print(d)               
d.nextDay()
print(d)               
d.nextDay()
print(d)              
d.previousDay()
print(d)               
d.nextMonth()
print(d)
d.nextYear()
print(d)