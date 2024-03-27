# class Calculator:
#     # self = refrence of an object 
#     def addition(self,x,y):
#         print(x,y)

#     def addition(self,x,y,z):
#         print(x,y,z)

#     def addition(self,x,y,z,a):
#         print(x,y,z,a)

#     def addition(self, x= None,y= None,z= None,a= None):
#      if(x !=None and y != None and z != None):
#         print(x+y+z+a)
#      elif(x != None and y != None and z != None):
#         print(x+y+z)
#      elif(x != None and y != None):
#         print(x+y)     


# cal =Calculator()
# cal.addition(23,45)
# cal.addition(23,45,66)
# cal.addition(23,45,66,78)          

#overloading
class Addition:
    def add(self,x,y):
        print(x+y)

    def add(self,x,y,z):
        print(x+y+z) 


    def add(self,x,y,z,a):
        print(x+y+z+a)  

    def add(self, x= None , y= None , z = None, a = None) :
            if x != None and y != None and z !=None and a != None:
                print(x+y+z+a)
            elif x != None and y != None and z !=None:
                 print(x+y+z)
            elif x != None and y != None:
                 print(x+y)     


a=Addition()
a.add(23,4)
a.add(234,56,67)
a.add(23,45,676,78)


#program 2
class Dog:
     def talk(self):
          print("bhow bhow")

class Human:
     def talk(self):
          print("hello hi")

def call_talk(obj):
     obj.talk()       


q1=Human()
q2=Dog()

call_talk(q1)
call_talk(q2)


#program 3
class Dog:
     def talk(self):
          print("bhow bhow")

class Human:
     def talk(self):
          print("hello hi")

class Car:
     def talk(self):
          print("brum brum")          

def call_talk(obj):
    if hasattr(obj,'talk'):
     obj.talk()       
    else:
        obj.sound()

q1=Human()
q2=Dog()
q3=Car()
call_talk(q1)
call_talk(q2)
call_talk(q3)
