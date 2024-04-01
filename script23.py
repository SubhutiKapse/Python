# program 1
# single inheritance 
# parent - constructor , child no constructor

class Student:
    def __init__(self,fn,ln,adharNo):
        self.firstName = fn 
        self.lastName = ln
        self.adharNo= adharNo

    def displayName(self):
        print(self.firstName  + self.lastName)

subhuti = Student("subhuti","kapse","123")
print(subhuti.firstName)
print(subhuti.lastName)
print(subhuti.adharNo)
subhuti.displayName()
        
class Teacher(Student):
    salary = 100000
    def displaySalary(self):
        print(self.salary)

subhutiA = Teacher("subhutiA","kapse2",123)

print(subhutiA.firstName)
print(subhutiA.lastName)
print(subhutiA.adharNo)
print(subhutiA.salary)

subhutiA.displayName()
subhutiA.displaySalary()

#program 2
#single inheritance
class Student:

    def __init__(self,fn,ln,adharNo):
        self.firstName = fn 
        self.lastName = ln 
        self.adharNo = adharNo

    def displayName(self):
        print(self.firstName + self.lastName)

class Teacher(Student):
    def __init__(self, fn, ln, adharNo,salary):
        super().__init__(fn, ln, adharNo)
        self.salary = salary

    def displaySalary(self):
        print(self.salary)


sapeksha = Teacher("sapeksha","kapse",123,343243243)
print(sapeksha.firstName)
print(sapeksha.lastName)
print(sapeksha.adharNo)
print(sapeksha.salary)

sapeksha.displayName()
sapeksha.displaySalary()
       
# program 3
# multi-level
class Student:
    def __init__(self,fn,ln,adharNo):
        self.firstName = fn 
        self.lastName = ln 
        self.adharNo = adharNo

    def displayName(self):
        print(self.firstName + self.lastName)

class Teacher(Student):
    def __init__(self,fn,ln,adharNo,salary):
        super().__init__(fn,ln,adharNo)
        self.salary = salary

    def displaySalary(self):
        print(self.salary)

class Professor(Teacher):
    def __init__(self, fn, ln, adharNo, salary,spec):
        super().__init__(fn, ln, adharNo, salary)
        self.special = spec

    def displaySpecialization(self):
        print(self.special)

bharat = Professor("bharat","bhate",213,4543534,"hindi")
print(bharat.firstName)
print(bharat.lastName)
print(bharat.adharNo)
print(bharat.salary)
print(bharat.special)

bharat.displayName()
bharat.displaySalary()
bharat.displaySpecialization()