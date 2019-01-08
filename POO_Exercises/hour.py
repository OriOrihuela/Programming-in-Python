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