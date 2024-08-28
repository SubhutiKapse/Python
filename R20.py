class Person:
    # class Level
    country = "India"
    count = 0

    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln
        Person.count =  Person.count


    # instance method
    def displayName(self):
        print(self.firstName+ self.lastName)

    @classmethod
    def changeCountry(cls):
        cls.country = "Bharatmata"

    @staticmethod
    def countObj():
        return Person.count
    
subhuti = Person("subhuti","kapse")
print(subhuti.country)
Person.changeCountry()
print(subhuti.country)
Person.countObj()


