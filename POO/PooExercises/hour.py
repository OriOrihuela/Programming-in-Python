class Hour():
    def __init__(self, hour, minutes, seconds):
        self.hour = 0
        self.minutes = 0
        self.seconds = 0
        try:
            self.hour = hour
            self.minutes = minutes
            self.seconds = seconds
            assert self.hour in range(0, 25) and self.minutes in range(0, 60) and self.seconds in range(0, 60)
        except AssertionError:
            self.hour = 0
            self.minutes = 0
            self.seconds = 0

    
    def setHour(self, hour):
        self.hour = hour
    def getHour(self):
        return self.hour
    
    def setMinutes(self, minutes):
        self.minutes = minutes
    def getMinutes(self):
        return self.minutes
    
    def setSeconds(self, seconds):
        self.seconds = seconds
    def getSeconds(self):
        return self.seconds
    

    def setFullHour(self, hour, minutes, seconds):
        try:
            self.hour = hour
            self.minutes = minutes
            self.seconds = seconds
            assert self.hour in range(0, 25) and self.minutes in range(0, 60) and self.seconds in range(0, 60)
        except AssertionError:
            self.hour = 0 
            self.minutes = 0
            self.seconds = 0
    
    def getFullHour(self):
        result = []
        for attribute in (self.__dict__):
            result.append(self.__dict__[attribute])
        return result
    
    def checkFullHour(self):
        result = ""
        for attribute in (self.__dict__):
            result += str(self.__dict__[attribute]) + ":"
        return result[:-1]


if __name__ == "__main__":
    

    # TEST CASES #


    new_hour = Hour(12, 30, 25)
    assert new_hour.getFullHour() == [12, 30, 25]
    assert new_hour.checkFullHour() == "12:30:25"

    new_hour_2 = Hour(15, 45, 61)
    assert new_hour_2.getFullHour() == [0, 0, 0]

    new_hour_3 = Hour(22,30,30)
    assert new_hour_3.getHour() == 22
    assert new_hour_3.getMinutes() == 30
    new_hour_3.setFullHour(23, 59, 59)
    assert new_hour_3.checkFullHour() == "23:59:59"