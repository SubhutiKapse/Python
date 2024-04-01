#bank 
#class level variable-country
#constructor-fn,ln,accNo transactions
#deposit(), withdrawl()
#static -total accounts
#class level for name change

class Bank:


    country="India"
    count=0


    def __init__(self,fn,ln,acc,bal):
        self.firstName=fn
        self.lastName=ln
        self.accNo=acc
        self.balance=bal
        self.transactions=[]
        Bank.count =Bank.count + 1

    def deposit(self,amount):
        self.balance =self.balance+amount
        self.transactions.append(amount)

    def withdrawl(self,amount):
        if(self.balance > amount):
            self.balance=self.balance-amount
            self.transactions.append(-amount)
        else:
            print("insufficient balance")

    def lastFiveTransactions(self,x):
        return self.transactions[-x::]  

    @classmethod
    def changeCountry(cls,cl):
        cls.country=cl


    @staticmethod
    def objCount():
        return Bank.count

subhuti=Bank("subhuti","kapse",111,10000000000000)        
sapeksha=Bank("sapeksha","singh",112,100000)
shyli=Bank("shyli","raj",113,10000)
sanvi=Bank("sanvi","shukla",114,10000)           


print(Bank.objCount())
subhuti.withdrawl(10000000000000)
subhuti.deposit(3000000000)
subhuti.deposit(30000)
subhuti.deposit(3000)
subhuti.deposit(300)
subhuti.deposit(30)
subhuti.deposit(3)
print(subhuti.lastFiveTransactions(4))