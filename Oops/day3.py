#class instance method
class Person:
    #constructor
    def __init__(self,fn,ln):
       #instance variable
        self.firstName=fn
        self.lastName=ln


        #instance method
    def displayName(self):
            print(self.firstName + self.lastName)

#lastNameUpdate
    def updateName(self,ln):
                self.lastName



subhuti=Person("subhuti","kapse")
print(subhuti.firstName)
print(subhuti.lastName)
subhuti.displayName()
subhuti.updateName("singh")

#class instance ,class method
class PersonB:
    country="India"
#constructor
    def __init__(self,fn,ln):
          #instance variable
          self.firstName=fn
          self.lastName=ln
              
              #instance method
    def updateName(self,fn,ln):
          self.firstName=fn
          self.lastName=ln

     #class method  
    @classmethod
    def updateCountry(cls,cnty):
        cls.country=cnty

q1=PersonB("sapeksha","pinjarkar")
print(q1.firstName)
print(q1.lastName)                   
print(q1.country)
q1.country="bharat"
q2=PersonB("sapeksha2","pinjarkar2")
print(q2.country)
PersonB.updateCountry('india B')

print(q1.country)
print(q2.country)

#static method
#count no of object
class PersonC:
    count=0
    country="Bharat" 

    def __init__(self,fn,ln):
        self.firstName=fn
        self.lastName=ln
        PersonC.count=PersonC.count+1

    def displayName(self):
        print(self.firstName + self.lastName)

    @classmethod
    def updateCountry(cls,cnty):
        cls.country = cnty

    @staticmethod
    def countObj():
        return PersonC.count

kamla = PersonC("kamla","raj")
vimla = PersonC("vimla","prakash")

a = PersonC.countObj()
print(a)

# bank class