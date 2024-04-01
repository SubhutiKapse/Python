# class  instance methof

class Person:

    #constructor
    def __init__(self,fn,ln):
        # instance variables
        self.firstName = fn 
        self.lastName = ln
    
    # instance method
    def displayName(self):
        print(self.firstName  + self.lastName)
    
    # lastNameUpdate
    def updateName(self,ln):
        self.lastName = ln


subhuti = Person("subhuti","kapse")
print(subhuti.firstName)
print(subhuti.lastName)
subhuti.displayName()
subhuti.updateName("dani")
# class instance , class method

class PersonB:
    country = "India"

    # constructor
    def __init__(self,fn,ln):
        # instance variable
        self.firstName = fn 
        self.lastName = ln

    # instance method
    def updateName(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln

    # class method
    @classmethod  
    def updateCountry(cls,cnty):
        cls.country = cnty  

h = PersonB("sapeksha","singh")
print(h.firstName)
print(h.lastName)
print(h.country)
h.country = "bharat"
h2 = PersonB("sapeksha2","singh2")
print(h2.country)
PersonB.updateCountry('india B')

print(h.country)
print(h2.country)


# static method 
# count number of objects 



class PersonC:
    count = 0
    country = "Bharat"

    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln
        PersonC.count =  PersonC.count  + 1


    def displayName(self):
        print(self.firstName+self.lastName)

    @classmethod
    def updateCountry(cls,cnty):
        cls.country = cnty

    @staticmethod
    def countObj():
        return PersonC.count

amol  = PersonC("amol","rao")
raj = PersonC("raj","kumar")

a = PersonC.countObj()
print(a)
# bank class