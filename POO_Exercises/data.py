class Data():
    
    def __init__(self, day, month, year):
        assert self.day in range(1,32) and self.month in range(1,13) and self.year in range(1900, 3001)
        self.day = 1
        self.month = 1
        self.year = 1900
        try:
            self.day = day
            self.month = month
            self.year = year
        except AssertionError:
            self.day = 1
            self.month = 1
            self.year = 1900
    

    def setDay(self, day):
        self.day = day
    def getDay(self, day):
        return self.day
    
    def setMonth(self, month):
        self.month = month
    def getMonth(self, month):
        return self.month
    
    def setYear(self, year):
        self.year = year
    def getYear(self, year):
        return self.year
    
    def setDate(self, day, month, year):
        assert self.day in range(1,32) and self.month in range(1,13) and self.year in range(1900, 3001)
        try:
            self.day = day
            self.month = month
            self.year = year
        except AssertionError:
            self.day = 1
            self.month = 1
            self.year = 1900
    
    def increaseDate(self, number):
        try:
            self.day += number
        except AssertionError:
            if self.day > 31:
                try:
                    self.day = 1
                    self.month += 1
                except AssertionError:
                    if self.month > 12:
                        self.month = 1
                        self.year += 1

    def printNameMonth(self, month):
        values = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        months = dict(zip(keys,values))
        if self.month in months:
            self.month = months[keys]

    def  printDate(self, day, month, year):
        return str(self.day) + ":" + printNameMonth(self.month) + ":" + str(self.year)
            
