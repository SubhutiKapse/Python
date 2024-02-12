#function without parameters and with returntype
def addA():
    print(9+9)

addA()
addA()    

#function with parameters andwithout returntype

def addB(x,y):
    print(x+y)
addB(2,4)
addB(4,7)    

#function with parameters and with returntype


def addC(x,y):
    return x+y
q1=addC(2,7)
print(q1)


#function without parameters and with returntype

def subA():
    print(9-9)


subA()
subA()
subA()


#function with parameters and without returntype

def subB(x,y):
    print(x-y)
subB(9,3)    


#function with parameter and returntype 

def subC(x,y):
    return x-y
w3=subC(9,3)
print(w3)



#function without parameters and with returntype


def addA():
    print(8+8)
addA()
addA()    


#function with parameters and without returntype
def addB(x,y):
    print(x+y)
addB(2,5)    

#function with parameters and with returntype

def addC(x,y):
    return x+y
q1=addC(9,9)
print(q1)

#function without parameters and with returntype
def addA():
    print(9+9)
addA()    

#function with parameters and without returntype
def addB(x,y):
    print(x+y)
addB(2,5)    


#function with parameters and with returntype


def addC(x,y):
    return x+y
q1=addC(2,9)
print(q1)


#function without parameters and with returntype
def addA():
    print(8+7)
addA()


#function with parameters and without returntype
def addB(x,y):
    print(x+y)
addB(2,5)    

#function with parameters and withreturntype

def addC(x,y):
    return x+y
q1=addC(4,6)
print(q1)

#conditional statement
#one input multiple outcomes


num=20
if num >0 and num <2:
    print("10 % discount")
if num <23 and num >24:
    print("20 % discount")    
if num >4 :
    print("30 % discount")    


    x1=10
    x2=23
    x3=44

# if x1 < x2 and x1 < x3:
#     print("x1 is greater")
# elif x2 > x1 and x2 < x3:
#  print("x2 is greater")
#  else:
#        print("x3 is greater")
    

x=20
print(x)    

h=[22,33,44,55,66]
print(h)
print(type(h))
print(len(h))

print(h[0])

names=["subhuti","shruti","shivmala","sugrata"]

print(names[0])
print(names[1])
print(names[2])
print(names[3])

for x in range(len(names)):
    print(names[x])


for y in names:
    print(y)


print("subhuti" in names)  


#function without parameters and with returntype
def addA():
    print(9+9)
addA()


#function with parameters and without returntype

def addB(x,y):
    print(x+y)

addB(9,3)



#function with parameters and without returntype
def addC(x,y):
  return x+y

a=addC(2,5)
print(a)

x=12
print(x)
print(type(x))


c="chinmay"
print(type[c])



h=[22,45,32,67,86]
print(h)
print(type(h))
print(len(h))

for x in range(len(h)):
    print(x)

for x in h:
    print(x)    

names=["subhuti","shruti","shivmala","sujata"]
print(names)
print(names[0])
print(names[1])
print(names[2])
print(names[3])

for x in range(len(names)):
    print(names[x])

for x in names:
    print(names)    


fruits=["apple","orange","banana","mango"]
print(fruits)
print(type(fruits))
print(len(fruits))

for item in fruits:
    print(item)

fruits[0]="apple"
print(fruits[0])    

vegetables=["tomato","potato","cauliflower","ladyfinger"]
print("tomato" in vegetables)
vegetables[0]="cabbage"
print(vegetables)


fruits=["apple","orange","banana","mango"]
fruits.append("papaya")
print(fruits)

fruits.insert(2,"straberry")
print(fruits)


fruits.remove("apple")
print(fruits)

animals=["tiger","lion","deer","monkey","rabbit","tiger"]

animals.count("tiger")
print(animals)

