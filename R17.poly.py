#POLYMORPHISM

# POLY---many
# morphism--one thing

#overloading
class Human:
    def talk(self):
        print("how you doing")

class Duck:
    def talk(self):
        print("quack quack")        

class Dog:
    def talk(self):
        print("bow bow")


def call_talk(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    else:
        obj.bark()

a = Human()
b = Duck()
c = Dog()


call_talk(c)
call_talk(b)
call_talk(a)





########################################



class Human:
    def talk(self):
        print("how you doing")

class Duck:
    def talk(self):
        print("quack quack")        

class Dog:
    def talk(self):
        print("bow bow")


def call_talk(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    else:
        obj.bark()

a = Human()
b = Duck()
c = Dog()
#d=Cat()# not define

call_talk(c)
call_talk(b)
call_talk(a)
#call_talk(d)