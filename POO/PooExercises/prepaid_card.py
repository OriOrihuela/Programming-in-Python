from hour import Hour

class PrepaidCard(Hour):

    def __init__(self, phone, dni, balance):
        self.phone = phone
        self.dni = dni
        self.balance = balance
        assert isinstance(self.phone, str) and isinstance(self.dni, str) and isinstance(self.balance, int)
        

    def setPhone(self, phone):
        self.phone = phone
    def getPhone(self):
        return self.phone
    
    def setDni(self, dni):
        self.dni = dni
    def getDni(self):
        return self.dni

    def getBalance(self):
        return self.balance
    

    def depositBalance(self, amount):
        self.balance += amount
    

    def sendMessage(self, numberMessagesToSend):
        cost = numberMessagesToSend * 0.09
        self.balance -= cost
    
    
    def makeCall(self, seconds):
        cost = 15 + (seconds * 0.01)
        self.balance -= cost

    

    def checkCard(self):
        for attribute in (self.__dict__):
            print("%s:%s" % (attribute, self.__dict__[attribute]))


if __name__ == "__main__":
    

    # TEST CASES #


    new_card = PrepaidCard("555666444", "98765432V", 500)
    new_card.depositBalance(500)
    new_card.sendMessage(10)
    assert new_card.getBalance() == 999.1
    assert new_card.getDni() == "98765432V"