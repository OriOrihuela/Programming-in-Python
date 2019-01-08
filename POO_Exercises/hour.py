class Hour():
    def __init__(self, hour, minutes, seconds):
        assert self.hour in range(0, 25) and self.minutes in range(0, 60) and self.seconds in range(0, 60)
        self.hour = 0
        self.minutes = 0
        self.seconds = 0
        try:
            self.hour = hour
            self.miutes = minutes
            self.seconds = seconds
        except AssertionError:
            self.hour = 0
            self.minutes = 0
            self.seconds = 0
    
    def setHour(self, hour):
        self.hour = hour
    def getHour(self, hour):
        return self.hour
    
    def setMinutes(self, minutes):
        self.minutes = minutes
    def getMinutes(self, minutes):
        return self.minutes
    
    def setSeconds(self, seconds):
        self.seconds = seconds
    def getSeconds(self, seconds):
        return self.seconds
    

    def setHour(self, hour, minutes, seconds):
        assert self.hour in range(0, 25) and self.minutes in range(0, 60) and self.seconds in range(0, 60)
        try:
            self.hour = hour
            self.minutes = minutes
            self.seconds = seconds
        except AssertionError:
            self.hour = 0 
            self.minutes = 0
            self.seconds = 0