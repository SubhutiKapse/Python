class Calculator:
    def addition(self,x,y):
        print(x+y)

    def addition(self,x,y,z):
        print(x+y+z)

    def addition(self,x,y,z,a):
        print(x+y+z+a)

    def addition(self , x = None , y = None , z = None , a = None):
        if(x != None and y != None  and z != None  and a != None):
            print(x+y+z+a)
        elif(x != None and y != None and z != None):
            print(x+y+z)
        elif(x != None and y != None):
            print(x+y)

cal = Calculator()
cal.addition(23,4)
cal.addition(23,4,5)
cal.addition(23,4,5,5)


#same class same method name , different signature

class Addition:

    def add(self,x,y):
        print(x+y)

    def add(self,x,y,z):
        print(x+y+z)
    
    def add(self,x,y,z,a):
        print(x+y+z+a)

    def add(self,x = None , y  = None , z = None , a = None):
            if  x != None and y != None and z != None and a != None :
                  print(x+y+z+a)
            elif x != None and y != None and z != None:
                  print(x+y+z)
            elif x != None and y != None:
                  print(x+y)



a = Addition()
a.add(12,3)
a.add(123,44,55)
a.add(23,4,5,6)


#program 2

class Dog:
    def talk(self):
        print("Bhow bhow")

class Human:
    def talk(self):
        print("Hello hi")

def call_talk(obj):
    obj.talk()


a = Human()
b = Dog()

call_talk(a)
call_talk(b)


# program 3

class Dog:
    def talk(self):
        print("Bhow bhow")

class Human:
    def talk(self):
        print("Hello hi")

class Duck:
    def sound(self):
        print("quack quack")

def call_talk(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    else:
        obj.sound()

a = Human()
b = Dog()
c = Duck()

call_talk(a)
call_talk(b)
call_talk(c)



print("hello" + "bye")
print(18 + 4)
print([21,22,23]+ [88,99,77])

class Bookx:
    def __init__(self,pages):
        self.pages = pages

    def __add__(self,other):
        return self.pages + other.pages
        

class Booky:
    def __init__(self,pages):
        self.pages = pages
        
    def __add__(self,other):
        return self.pages + other.pages

ramayan  = Bookx(120)
mahabharat =  Booky(45)
#print(ramayan.pages + mahabharat.pages)
print(ramayan + mahabharat)
print(mahabharat + ramayan)


#program 2
print(4 > 2)

class Bookx:
    def __init__(self,pages):
        self.pages = pages
    def __gt__(self,others):
        return self.pages > others.pages

class Booky:
    def __init__(self,pages):
        self.pages = pages
    def __lt__(self,others):
        return self.pages > others.pages

ram = Bookx(120)
sham = Booky(130)

print(ram.pages > sham.pages)
print(ram > sham)
#print(ram < sham)

class WorkBank:
    def loan(self):
        print("I am loan from WB")
    def save(self):
        print('I am save from WB')

class SBI(WorkBank):
    def loan(self):
        print("I am loan from SBI")
        super().loan()
    def save(self):
        print('I am save from SBI')
        super().loan()
    

class PNB(WorkBank):
    def loan(self):
        print("I am loan from SBI")
        super().loan()
    def save(self):
        print('I am save from SBI')
        super().save()
      
a = SBI()
a.loan()
a.save()