class Person:
    def __init__(self,fn,ln):
        self.firstName=fn
        self.lastName=ln

    def display_name(self):
        print(self.firstName + self.lastName) 
subhuti=Person("subhuti","kapse")  
sapeksha=Person("Ajay","kapse")
print(subhuti.firstName)
print(sapeksha.firstName)
print(sapeksha.lastName)
print(subhuti.lastName)
sapeksha.display_name()
subhuti.display_name()

#person 2
class Person2:
    country ="bharat"
    def __init__(self,fn,ln):
        self.firstName=fn
        self.lastName=ln
    def displayName(self):
        print(self.firstName + self.lastName)


    @classmethod
    def changeCountry(cls,cnty):
        cls.country=cnty

subhuti=Person2("subhuti","kapse")
sapeksha=Person2("sapeksha","singh")
shyli=Person2("shyli","solanki")  

print(subhuti.firstName)
print(subhuti.lastName)
print(subhuti.country)
subhuti.country="India"
print(subhuti.country)
print(sapeksha.country)
print(shyli.country)
Person2.changeCountry("Hindustan")
print(subhuti.country)
print(sapeksha.country)
print(shyli.country)