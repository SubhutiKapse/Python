# # class Person4:
# #     first_name=None
# #     last_name=None
# #     age=None
# #     rollno=None

# # def display_name(self):
# #     print(self.first_name + self.last_name)    

# # subhuti=Person4()
# # print(subhuti.first_name)
# # print(subhuti.last_name)
# # print(subhuti.age)
# # print(subhuti.rollno)


# # subhuti.first_name="shyli"
# # subhuti.last_name="singh"
# # subhuti.age=21
# # subhuti.rollno=11162
# # subhuti.display_name()


# # Setting the value at the time of object creation
# class Person5:
#     def __init__(self,fn,ln,ag,rn) :
#         self.firstName=fn
#         self.lastName=ln
#         self.age=ag
#         self.rollNo=rn


# def displayName(self):
#     print(self.firstName +self.lastName)

# subhuti=Person5("sanu","rana",21,234)
# print(subhuti.firstName)
# print(subhuti.lastName)
# print(subhuti.age)



# #########################

# # instance method - instance variables
# class Person:
#     # class variable
#     country = "india"

#     def __init__(self,fn,ln,ag):
#         self.firstName  = fn 
#         self.lastName = ln 
#         self.age = ag

#     # instance method
#     def displayName(self):
#         print(self.firstName + self.lastName)

#     # instance
#     def changeFirstName(self,rfn):
#         self.firstName = rfn

# subhuti= Person("subhuti","kapse",23)
# annu = Person("annu","radha",34)

# print(subhuti.age)
# print(subhuti.firstName)
# print(subhuti.lastName)
# print(subhuti.country)
# subhuti.displayName()
# subhuti.country  = "bharat"

# print(annu.country)
# print(subhuti.country)

# # class methods -- className -- change common or class variables

# class Person:
#     # class variable
#     country = "india"

#     def __init__(self,fn,ln,ag):
#         # instance vraible
#         self.firstName = fn 
#         self.lastName = ln 
#         self.age = ag
    
#     # instance method
#     def displayName(self):
#         print(self.firstName + self.lastName)

#     @classmethod
#     def changeCountry(cls,cc):
#         Person.country = cc


# sani = Person("sani","ranta",23)
# damini = Person("subhuti","kapse",34)

# print(sani.firstName)
# print(sani.lastName)
# print(sani.age)
# print(sani.country)


# print(subhuti.firstName)
# print(subhuti.lastName)
# print(subhuti.age)
# print(subhuti.country)

# Person.changeCountry("bharat")
# print(subhuti.country)
# print(damini.country)

# subhuti.country = "IND"

# print(subhuti.country)


class Person:
    firstName = None
    lastName = None 
    age = None 
    rollNo = None

    def displayName(self):
        print(self.firstName + self.lastName)


subhuti=Person()        

subhuti.firstName="subhuti"
subhuti.lastName="kapse"
subhuti.age=21
subhuti.rollNo=221


print(subhuti.firstName)
print(subhuti.lastName)
print(subhuti.age)
print(subhuti.rollNo)

# #class using constructor

# class Person:
#     def __init__(self,fn,ln,ag,rn):
#         self.firstName=fn
#         self.lastName=ln
#         self.age=ag
#         self.rollNo=rn

# def displayName(self):
#     print(self.firstName + self.lastName)        


# subhuti=Person("subhuti","kapse",21,221)
# sanu=Person("sanu","sani",22,2434)
# sanu.displayName()
# subhuti.displayName()


        
# #constructor

# class Bank:
#     def __init__(self,fuln,accno,bal):
#         self.fullName=fuln
#         self.accNO=accno
#         self.balance=bal
#         self.transactions=[]


# #for deposit
# def deposit(self,amt):
#     self.balance=self.balance+amt
#     self.transactions.append(amt)
#     return self.balance
# #for withdrawl

    
# def withdrawl(self,amt):
#  if amt < self.balance:
#     self.balance = self.balance - amt
#     self.transactions.append(-amt)
#     return self.balance
#  else:
#     print("Insufficient balance :"+str(self.balance))


# # lastFive transactions
# def lastFiveTransactions(self):
#     return self.transactions[-5::]

# # lastten transactions
# def lasttenTransactions(self):
#    return self.transactions[-10::]

# subhuti=Bank("subhuti kapse",21,123)
# subhuti.deposit(100)

# subhuti.withdrawl(5)
# subhuti.deposit(1000)
# subhuti.withdrawl(50)

# print(subhuti.lastFiveTransactions())
# print(subhuti.transactions)









##########################################


# instance method
class Person:
    def __init__(self,fn,ln,ag):
        # instance variables
        self.firstName = fn 
        self.lastName = ln 
        self.age = ag
    # instance method to print fullName
    def displayName(self):
        print(self.firstName + self.lastName)
    # instance method to update age
    def updateAge(self,ag):
        self.age = ag


subhuti = Person("subhuti","kapse",21)
print(subhuti.firstName)
print(subhuti.lastName)
print(subhuti.age)
subhuti.displayName()
subhuti.updateAge(23)
print(subhuti.age)

sanu = Person("sanu","soni",22)
sanu.displayName()
sanu.updateAge(34)
print(sanu.age)

# class method 

class PersonB :
    # class level variable
    country = "india"
    def __init__(self,fn,ln,ag):
        # instance varibales
        self.firstName = fn 
        self.lastName = ln 
        self.age = ag 

    # instance method
    def displayName(self):
        print(self.firstName + self.lastName)

    # class method
    @classmethod
    def changeCountry(cls,cn):
        cls.country = "bharat"

subhuti  = PersonB("subhuti","kapse",21)
sapeksha = PersonB("sapeksha","pure",22)
print(subhuti.firstName)
print(subhuti.lastName)
print(subhuti.age)
print(subhuti.country)
subhuti.country = "bharat"
print(sapeksha.country)
print(subhuti.country)

PersonB.changeCountry('bharat')

shruti = PersonB("shruti","kapse",17)
print(shruti.country)

# static method
# static methods are called directly on className

class Counter:
    # class variable
    count = 0
    # constructor
    def __init__(self):
        Counter.count =   Counter.count  + 1

    @staticmethod
    def countObj():
        return Counter.count
    
subhuti = Counter()
sapeksha = Counter()

e = Counter.countObj()
print(e)

        