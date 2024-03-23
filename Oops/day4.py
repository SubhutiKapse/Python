#program 1
#single inheritance
#parent - constructor,child no constructor
# class Student:
#     def __init__(self,fn,ln,adharNo):
#         self.firstName = fn 
#         self.lastName = ln
#         self.adharNo= adharNo

#     def displayName(self):
#         print(self.firstName  + self.lastName)

# #subhuti = Student("subhuti","kapse","123")
# # print(subhuti.firstName)
# # print(subhuti.lastName)
# # print(subhuti.adharNo)
# # subhuti.displayName()
        
# class Teacher(Student):
#     salary = 100000
#     def displaySalary(self):
#         print(self.salary)

# subhuti2 = Teacher("subhuti2","kapse2",123)
# print(subhuti2.firstName)
# print(subhuti2.lastName)
# print(subhuti2.adharNo)
# print(subhuti2.salary)

# amolT.displayName()
# amolT.displaySalary()

# program 2
# single inheritance
# class Student:

#     def __init__(self,fn,ln,adharNo):
#         self.firstName = fn 
#         self.lastName = ln 
#         self.adharNo = adharNo

#     def displayName(self):
#         print(self.firstName + self.lastName)

# class Teacher(Student):
#     def __init__(self, fn, ln, adharNo,salary):
#         super().__init__(fn, ln, adharNo)
#         self.salary = salary

#     def displaySalary(self):
#         print(self.salary)


# subhuti3 = Teacher("subhuti3","kapse3",123,343243243)
# print(subhuti3.firstName)
# print(subhuti3.lastName)
# print(subhuti3.adharNo)
# print(subhuti3.salary)

# subhuti3.displayName()
# subhuti3.displaySalary()

      
# program 3
# multi-level

class Student:
    def __init__(self,fn,ln,adharNo):
        self.firstName=fn
        self.lastName=ln
        self.adharNo=adharNo

    def displayName(self):
        print(self.firstName + self.lastName)

class Teacher(Student):
    def __init__(self, fn, ln, adharNo,salary):
        super().__init__(fn, ln, adharNo) 
        self.salary=salary

    def displaySalary(self):
        print(self.salary) 

class Professor(Teacher):
    def __init__(self, fn, ln, adharNo, salary,spec):
        super().__init__(fn, ln, adharNo, salary)
        self.special=spec

    def displaySpecialization(self):
      print(self.special)
            

sapeksha=Professor("sapeksha","singh",111,3844545949,"english")
print(sapeksha.firstName)
print(sapeksha.lastName)
print(sapeksha.adharNo)
print(sapeksha.salary)
print(sapeksha.special)

sapeksha.displayName()
sapeksha.displaySalary()
sapeksha.displaySpecialization()