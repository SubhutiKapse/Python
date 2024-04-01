class Person:
    def __init__(self,fn,ln):
        self.firstName  = fn 
        self.lastName = ln

    def display_name(self):
        print(self.firstName + self.lastName)
class Person:
    def __init__(self,fn,ln):
        self.firstName  = fn 
        self.lastName = ln

    def display_name(self):
        print(self.firstName + self.lastName)

subhu = Person("subhu","kapse")
sanu = Person("sanu","rai")   
print(subhu.firstName)
print(sanu.firstName)
print(sanu.lastName)
print(subhu.lastName)
sanu.display_name()
subhu.display_name()

# program 2

class Person2:
    country = "bharat"
    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln
    def displayName(self):
        print(self.firstName + self.lastName)

    @classmethod
    def changeCountry(cls,cnty):
        cls.country = cnty

sneha = Person2("sneha","raichad")
shalakha = Person2("shalakha","rute")
shagun = Person2('shagun',"shani")

print(sneha.firstName)
print(sneha.lastName)
print(sneha.country)
sneha.country = "india"
print(sneha.country)
print(shalakha.country)
print(shagun.country)
Person2.changeCountry("Hindustan")
print(sneha.country)
print(shalakha.country)
print(shagun.country)












   