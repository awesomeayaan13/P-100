class Atm():
    def __init__(self,cardNumber,pinNumber):
        self.cardNumber=cardNumber
        self.pinNumber=pinNumber


    def withdrawMoney(self):
        print("Enter the amount to withdraw:")
    
    def bankBalance(self, cardNumber, pinNumber):
        return self.cardNumber

        
BrokePerson=Atm(913,5888)
BrokePerson.withdrawMoney()
BrokePerson.BankBalance(913,5888)
