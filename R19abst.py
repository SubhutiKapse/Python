# #ABSTRACTION


# #from xyz import XYZ ,abstractmethod

# class Demo(XYZ):
#     @abstractmethod
#     def loan(self):
#         pass

#     def save(self):
#      pass



# class SBI(Demo):
#     def loan(self):
#         print("loan mathod")


 

# class PNB(Demo):
#     pass    
# q1=SBI()         



# #what is abstract class---we cannot create obj id AC

# from abc import ABC , abstractmethod

# class wordBank(ABC):

#     @abstractmethod
#     def save(self):
#         pass

#     @abstractmethod
#     def loan(self):
#         pass

# class SBI(wordBank):
#     def save(self):
#         print("SBI save")
#     def loan(self):
#         print("SBI loan")
#     def branchSBI():
#         print("SBI branch")

# class PNB(wordBank):
#     def save(self):
#         print("PNB save")
#     def loan(self):
#         print("PNB loan")
#     def branchPNB():
#         print("PNB branch")
# wb1 = SBI()
# wb2 = PNB()

# #wb1 = wordBank()

# class basicInfo(ABC):
#     @abstractmethod
#     def fullName(self):
#         pass
#     @abstractmethod
#     def occupation(self):
#         pass
#     def country(self):
#         print('india')


# class Person(basicInfo):
#     def fullName(self):
#         print("Personone")
#     def occupation(self):
#         print("Student")


# class Person2(basicInfo):
#     def fullName(self):
#         print("Persontwo")
#     def occupation(self):
#         print("Teacher")

# a = Person()
# a.country()
# a.fullName()
# a.occupation()




#method order resolution---multiple order R

class A(object):
    def methodOne(self):
        print("A class is called")
        super().methodOne()

class B(object):
    def methodOne(self):
        print("B class is called")
        super().methodOne()

class C(object):
    def methodOne(self):
        print("C class is called")

class X(A,B):
    def methodOne(self):
         print("Class X is called")
         super().methodOne()

class Y(B,C):
    def methodOne(self):
         print("Class Y is called")
         super().methodOne()

class P(X,Y,C):
    def methodOne(self):
         print("Class P is called")
         super().methodOne()


p =P()
p.methodOne()
