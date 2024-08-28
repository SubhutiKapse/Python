# #INHERITANCE


# #SINGLE -INHERITANCE---single parent single child
# #MULTI-LEVEL INHERITANCE
# #MULTIPLE -INHERITANCE
# #HIERARCHICAL- INHERITANCE

# #SINGLE -INHERITANCE--- parent with constructor, child with nio constructor
# class Student:
#     firstName="subhuti"
#     lastName="kapse"
#     adharCard=76558465

# def displayName(self):
#     print(self.firstName + self.lastName)    

# class Teacher:
#     firstName="subhuti"
#     lastName="kapse"
#     adharCard=76558465
#     salary=200000000000000

# def displayName(self):
#     print(self.firstName + self.lastName)  

# def displaySalary(self):
#     print(self.salary)      



# subhuti=Teacher()
# print(subhuti.firstName)
# print(subhuti.lastName)
# print(subhuti.adharCard)
# print(subhuti.salary)
# #subhuti.displayName()
# #subhuti.displaySalary()

# subhuti=Student()
# print(subhuti.firstName)
# print(subhuti.lastName)
# print(subhuti.adharCard)



# class Student:
#     def __init__(self,fn,ln):
#         self.firstName = fn 
#         self.lastName = ln
    
#     def displayName(self):
#         print(self.firstName + self.lastName)

# class Teacher(Student):
#     def __init__(self,fn,ln,salary):
#         super().__init__(fn,ln)
#         self.salary = salary
    
#     def displaySalary(self):
#         print(self.salary)

# rani = Teacher("rani","mehta",2444)
# print(rani.firstName)
# print(rani.lastName)
# print(rani.salary)
# rani.displayName()
# rani.displaySalary()

# #MULTI-LEVEL INHERITANCE--parent and child with constructor

# class GrandFather:
#     def __init__(self,fn,ln):
#         self.firstName = fn 
#         self.lastName = ln

#     def displayName(self):
#         print(self.firstName + self.lastName)


# class Father(GrandFather):
#     def __init__(self,fn,ln,ffn):
#         super().__init__(fn,ln)
#         self.fname = ffn
    
#     def displayFName(self):
#         print(self.fname + self.lastName)

# class Daughter(Father):
#     def __init__(self, fn, ln, ffn,ssn):
#         super().__init__(fn, ln, ffn)
#         self.sname = ssn

#     def displaySname(self):
#         print(self.sname + self.lastName)

# subhuti = Daughter("vasu","kapse","ajay","subhuti")
# print(subhuti.firstName)
# print(subhuti.lastName)
# print(subhuti.sname)
# print(subhuti.fname)

# subhuti.displayFName()
# subhuti.displayName()
# subhuti.displaySname()














#SINGLE _INHERITANCE
class Student:
    def __init__(self,fn,ln) :
        self.firstName=fn
        self.lastName=ln

    def displayName(self):
        print(self.firstName +self.lastName)   

class Teacher(Student):
    def __init__(self,fn,ln,salary):
     super().__init__(fn,ln)
     self.salary=salary


    def displaySalary(self):
        print(self.salary)    


subhutiA=Teacher("subhutiA","kapse","2000")
print(subhutiA.firstName)
print(subhutiA.lastName)
print(subhutiA.salary)
subhutiA.displaySalary()
subhutiA.displayName()          






#MULTIPLE -INHERITANCE
class GrandFather:
    def __init__(self,fn,ln):
       self.firstName=fn
       self.lastName=ln

    def displayName(self):
        print(self.firstName + self.lastName)   

class Father(GrandFather):
    def __init__(self,fn,ln,ffn):
     super().__init__(fn,ln)
     self.fname=ffn

    def displayFname(self):
        print(self.fname + self.lastName)   


class Daughter(Father):
   
    def __init__(self,fn,ln,ffn,ddn):
     super().__init__(fn,ln,ffn)
       
     self.dname=ddn

    def displayDname(self):
        print(self.dname + self.lastName)   


subhutiB=Daughter("veer","kapse","ajay","subhutiB")
print(subhutiB.firstName)
print(subhutiB.lastName)
print(subhutiB.dname)


subhutiB.displayName()
subhutiB.displayFname()
subhutiB.displayDname()



#HIERARCHICAL- INHERITANCE--one parent two child

class Mother:
   def __init__(self,fn,ln) -> None:
    self.firstName=fn
    self.lastName=ln

   def displayMname(self):
       print(self.firstName + self.lastName)


class Son(Mother):
    def __init__(self, fn, ln,ssn):
      super().__init__(fn, ln)
      self.sname=ssn


    def displaySname(self):
        print(self.firstName + self.lastName)


        
class Daughter(Mother):
    def __init__(self, fn, ln,ddn):
      super().__init__(fn, ln)
      self.dname=ddn


    def displayDname(self):
        print(self.firstName + self.lastName)


SubhutiC=Daughter("karan","kapse","subhuti")
raj=Son("karan","kapse","raj")


print(SubhutiC.firstName)
print(SubhutiC.lastName)
print(SubhutiC.dname)

SubhutiC.displayDname()
SubhutiC.displayMname()

print(raj.firstName)
print(raj.lastName)
print(raj.sname)

raj.displayMname()
raj.displaySname()



# # overloading 
# # same class , same method but different signature - overriding

class Calculator:
 def addition(self,x,y):
  print(x+y)

 def addition(self,x,y,z):
  print(x+y+z)

def addition(self,x,y,z,a):
  print(x+y+z+a)
def addition(self,x= None, y = None , z = None , a = None):
        if x != None and y != None and z != None and a != None:
           print(x+y+z+a)
        elif x != None and y != None and z != None:
           print(x+y+z)
        elif x != None and y != None:
           print(x+y)
        

e = Calculator()
e.addition(12,3)
e.addition(12,3,3)
e.addition(12,3,3,4)        


# # overriding 
# # same methodname , same signature but different class 
# # has a relationship

class WorldBank:
    def save(self):
      print("I am from worlbank")

    def loan(self):
      print("i am loan from worldbank")
    

class SBI(WorldBank):
    def save(self):
      print("I am from SBI")

    def loan(self):
      print("i am loan from SBI")
    

e = SBI()
e.loan()
e.save()


# # operator overloading
# # print(1 + 1)
# # print("hello "+ "world!")
# # print(2 + "hello")
# # # print(obj + obj)

# print(1 + 1)
# print("hello "+ "world")
# # operator overloading

# # class BookX:
def __init__(self,pages):
        self.pages = pages
    
# #     # addition operator overloaded to get result of adding object
def __add__(self,others):
         return self.pages + others.pages

class BookY:
     def __init__(self,pages):
      self.pages = pages
     def __add__(self,others):
         return self.pages + others.pages
    

mahabharat = BookY(120)
ramayan = BookY(240)

print(mahabharat.pages + ramayan.pages)
print(mahabharat+ramayan)
print(ramayan+mahabharat)


class BookY:
    def __init__(self,pages):
      self.pages = pages

class BookX:
    def __init__(self,pages):
       self.pages = pages

    def __gt__(self,other):
       return self.pages > other.pages 


x = BookX(30)
y = BookY(25)
print(x.pages > y.pages)
print(x > y)
