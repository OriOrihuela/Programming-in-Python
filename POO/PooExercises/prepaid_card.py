class PrepaidCard():

    def __init__(self, phone, dni, balance, consumption):
        self.phone = phone
        self.dni = dni
        self.balance = balance
        self.consumption = consumption
        

    def setPhone(self, phone):
        self.phone = phone
    def getPhone(self):
        return self.phone
    
    def setDni(self, dni):
        self.dni = dni
    def getDni(self):
        return self.dni

    def setBalance(self, balance):
        self.balance = balance
    def getBalance(self):
        return self.balance
    
    def setConsumption(self, consumption):
        self.consumption = consumption
    def getConsumption(self):
        return self.consumption