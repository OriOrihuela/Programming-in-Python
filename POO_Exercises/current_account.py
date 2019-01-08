class CurrentAccount():

    def __init__(self, name, surname, direction, phone, balance):
        self.name = name
        self.surname = surname
        self.direction = direction
        self.phone = phone
        self.balance = balance
        self.red_numbers = False
    


    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    
    def setSurname(self, surname):
        self.surname = surname
    def getSurame(self):
        return self.surname
    
    def setDirection(self, direction):
        self.direction = direction
    def getDirection(self):
        return self.direction
    
    def setPhone(self, phone):
        self.phone = phone
    def getPhone(self):
        return self.phone
    
    def setBalance(self, balance):
        self.balance = balance
    def getBalance(self):
        return self.balance
    

    def setWithdrawMoney(self, amount):
        self.balance -= amount
        return self.balance
    
    def setDepositMoney(self, amount):
        self.balance += amount
        return self.balance
    
    def checkAccount(self):
        for attribute in (self.__dict__):
            print("%s : %s" % (attribute, self.__dict__[attribute]))
    
    def red_Numbers(self):
        if self.balance < 0:
            self.red_numbers = True
        else:
            self.red_numbers = False


if __name__ == "__main__":
    

    # TEST CASES #

    account_Edu = CurrentAccount("Eduardo", "Orihuela Verdugo", "C/ Pepinaso, 6", "987654321", 1000)
    assert account_Edu.setDepositMoney(500) == 1500
    account_Edu.checkAccount()
    
    account_Toni = CurrentAccount("Toni", "March Marti", "C/ Caraculo, 8", "789456123", 500)
    assert account_Toni.setWithdrawMoney(250) == 250
    account_Toni.checkAccount()