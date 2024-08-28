#DUCK TYPING

class Human:
    def talk(self):
        print("hi myself human")

class Duck:
    def talk(self):
        print("quack quack")

class Dog:
    def bark(self):
        print("bow bow")                


def call_talk_other(obj):
    if hasattr(obj,"talk"):
        obj.talk()
    elif hasattr(obj,"bark"):
       obj.bark()

q1=Human()
q2=Dog()
q3=Duck()


call_talk_other(q1)
call_talk_other(q2)
call_talk_other(q3)



#overloading---same class --same methoad but diff sig/para
#overriding---same methodname---same sig/para but diff class---Inheritance


#overloading

class Calculator:
    # def addition(self,x,y):
    #   print(x+y)

    # def addition(self,x,y,z):
    #   print(x+y+z)

    # def addition(self,x,y,z,a):
    #   print(x+y+z+a)
    def addition(self,x= None, y = None , z = None , a = None):
        if x != None and y != None and z != None and a != None:
           print(x+y+z+a)
        elif x != None and y != None and z != None:
           print(x+y+z)
        elif x != None and y != None:
           print(x+y)
        
a1 = Calculator()
a1.addition(10,3)
a1.addition(10,3,3)
a1.addition(10,3,3,4)




# overriding
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
    

p = SBI()
p.loan()
p.save()