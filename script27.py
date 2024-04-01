# bank 
# class level variable - country
# constructor  - fn , ln , accNo transactions
# deposit() , withdrawl()
# static - total accounts
# class level for name change


class Bank:

    country = "India"
    count = 0

    def __init__(self,fn,ln,acc,bal):
        self.firstName = fn 
        self.lastName = ln 
        self.accNo = acc
        self.balance = bal
        self.transactions = []
        Bank.count = Bank.count + 1
    
    def deposit(self,amount):
        self.balance = self.balance + amount
        self.transactions.append(amount)

    def withdrawl(self,amount):
        if(self.balance > amount):
            self.balance  = self.balance - amount
            self.transactions.append(-amount)
        else:
            print("insufficient balance")

    def lastFiveTransaction(self,x):
        return self.transactions[-x::]

    @classmethod
    def changeCountry(cls,cl):
        cls.country  = cl 

    @staticmethod
    def objCount():
        return Bank.count
    
subhuti  = Bank("subhuti","kapse",123,1000)   
sapeksha  = Bank("sapeksha","singh",123,1000)   
shivani  = Bank("shivani","rai",123,1000)   
shruti  = Bank("shruti","vyas",123,10000000)   
sanvi  = Bank("sanvi","vijay",123,100000000)   

print(Bank.objCount())
subhuti.withdrawl(1000000000)
subhuti.deposit(30000000)
subhuti.deposit(30000)
subhuti.deposit(3000)
subhuti.deposit(30)
subhuti.deposit(3)
print(subhuti.lastFiveTransaction(2))