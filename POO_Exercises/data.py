class Data():
    
    def __init__(self, day, month, year):
        assert day == int and month == int and year == int
        assert day in range(1,32) and month in range(1,13) and year in range(1900, 3001)
        try:
            self.day = 1
            self.month = 1
            self.year = 1900
        except ValueError:
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
    
