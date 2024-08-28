#FUNCTION


#function is a self contained block of code which performs predefined tasks

#int as parameter and int as a return type
def sub(x,y):
    return x-y
q1=sub(5,2)
print(q1)
print(type(q1))

# int as parameter and int as a return type 
def add(x,y):
    return x + y
q1 = add(12,3)
print(q1)

#float as parameter and int as a return type
def subA(x,y):
    return x-y
q2=subA(5.2,2.3)
print(q1)

# float as a parameter and float as a return type 
def add2(x,y):
    return x + y
q2 = add2(12.3,45.6)
print(q2)

#boolean as parameter and int as a return type
def canDrive(age,haveVehicle):
    if age >=18 and haveVehicle:
        return True
    else:
        return False
q3=canDrive(18,True)    
print(q3)

# boolean as a parameter and boolean as return type 
def canDrive(age,haveVehicle):
    if age >= 18 and haveVehicle:
        return True 
    else:
        return False
q4 = canDrive(18,True)
print(q4)

#string as parameter and int as a return type
def greet(name):
    return "welcome "+name+" !"
q4=greet("subhuti")
print(q4)

# string as a paramter and string as a return
def greet(word):
    return "hello "+ word
q3 = greet("chinmay")
print(q3)

#list as parameter and int as a return type
fruits=["apple","banana","orange","straberry"]
def addFruits(lst):
    lst.append("kivi")
    return lst
q5=addFruits(fruits)
print(q5)

# list as parameter and list a return type 
def addCity(lst):
    lst.append("nagpur")
    return lst
q5 = addCity(["wardha","pune","mumbai"])
print(q5)

#dict as parameter and int as a return type
info = {
    "firstName":"subhuti",
    "lastName":"kapse",
    "age":21
}

def addLangauge(d):
    d.update({"language":"marathi"})
    return d
q6 = addLangauge(info)
print(q6)

# dictionary as a parameter and dictionary as a return type 

info = {
    "firstName":'chinmay',
    "lastName":"deshpande"
}
def addCity(info):
    info['city'] = "pune"
    return info
q6 = addCity(info)
print(q6)
#tuple as parameter and int as a return type
tupC = (11,22,33)
def addElementToTuple(tupA):
    tupA = list(tupA)
    tupA.append(44)
    tupA = tuple(tupA)
    return tupA
q7 = addElementToTuple(tupC)
print(q7)

# tuple as a parameter and tuple as a return type 
g  =(11,22,33)
def addElement(tp):
    tp = list(tp)
    tp.append(44)
    tp = tuple(tp)
    return tp
q7 = addElement(g)
print(q7)


#set as parameter and int as a return type
setA = {11,22,33}
def addValToSet(setP):
    setP.add(44)
    return setP
q8 = addValToSet(setA)
print(q8)


#set as parameter and int as a return type
setA = {11,22,33}
def removeElement(setR):
    setR.remove(33)
    return setR
q8 = removeElement(setA)
print(q8)



# program 1
# int as parameter and int as a return type 
def add(x,y):
    return x + y
q1 = add(12,3)
print(q1)


#program 2
# float as a parameter and float as a return type 
def add2(x,y):
    return x + y
q2 = add2(12.3,45.6)
print(q2)

#program 3
# string as a paramter and string as a return
def greet(word):
    return "hello "+ word
q3 = greet("chinmay")
print(q3)

#program 4
# boolean as a parameter and boolean as return type 
def canDrive(age,haveVehicle):
    if age >= 18 and haveVehicle:
        return True 
    else:
        return False
q4 = canDrive(18,True)
print(q4)

#program 5
# list as parameter and list a return type 
def addCity(lst):
    lst.append("nagpur")
    return lst
q5 = addCity(["wardha","pune","mumbai"])
print(q5)

#program6
# dictionary as a parameter and dictionary as a return type 

info = {
    "firstName":'chinmay',
    "lastName":"deshpande"
}
def addCity(info):
    info['city'] = "pune"
    return info
q6 = addCity(info)
print(q6)

# program 7
# tuple as a parameter and tuple as a return type 
g  =(11,22,33)
def addElement(tp):
    tp = list(tp)
    tp.append(44)
    tp = tuple(tp)
    return tp
q7 = addElement(g)
print(q7)

# set as a parameter and set as a return type 
setA = {11,22,33}
def removeElement(setR):
    setR.remove(33)
    return setR
q8 = removeElement(setA)
print(q8)

# lambda function
# lamdba - keyword
# x , y - parameter 
# x + y - return 
add = lambda x,y:x+y
print(add(12,3))

sqrt = lambda x : x * x
print(sqrt(12))

cube  = lambda x: x * x * x
print(cube(9))

# function as a parameter

sub = lambda x,y:x-y

def subtraction(fn,x,y):
    # x = 24 
    # y = 12
    # fn = lambda x,y:x-y
    e = fn(x,y)
    return e

q9 = subtraction(sub,24,12)
print(q9)


add = lambda x , y : x + y
def addition(fn,x ,y):
    # x - 12
    # y - 3 
    # fn = lambda x , y : x + y
    e = fn(x,y)
    return e
q10 = addition(add,12,3)
print(q10)






# # int 
# # int as a parameter and int as a return type 
# def add(x,y):
#     return x + y

# e = add(12,3)
# print(e)
# print(type(e))

# # float 
# # float value as a parameter and float value as return type 
# def addB(x,y):
#     return x + y
# f = addB(12.4,13.4)
# print(f)
# print(type(f))

# boolean value as a parameter and boolean value as a return type
# boolean 
print("hello")
def CanDrive(age, hvV):
    if age >= 18 and hvV:
        return True
    else:
        return False
f = CanDrive(13,True)
print(f)

# string 
# string as a parameter and string as a return type 
def greet(word):
    return "hello "+ word
g  = greet("subhuti")
print(g)

# list 
# list a parameter and list a return type 

names = ["subhuti","subhu","sani","shweta"]
def addE(lst):
    lst.append("sapeksha")
    return lst
j = addE(names)
print(j)

# dict 
# dict as a parameter and dict as a return type 
info = {
    "firstName":"subhuti",
    "lastName":"kapse",
    "age":21,
    "rollNo":344
}

def addEtoD(information):
    information['language'] = "marathi"
    information.update({"city":"banglore"})
    return information
h = addEtoD(info)
print(h)

# tuple
# tuple as a parameter and tuple as a return type
tupleA = (12,34)
print(type(tupleA))
def addE(tupB):
    tupB = list(tupB)
    tupB.append(56)
    tupB = tuple(tupB)
    return tupB
l = addE(tupleA)
print(l)

# set 
# set as a parameter and set as a return type 
g = {11,22,33,44,55,66}
def addV(setB):
    setB.add(35)
    return setB
w = addV(g)
print(w)



# expression
def add(x,y):
    return x + y
e = add(12,4)
print(e)

# lambda --- keyword
# x , y  --- parameter 
# x + y  --- return type 


add = lambda x,y:x+y
e = add(34,5)
print(e)

# program 2

x = 10
print(x)

f = lambda x : x * x
#print(f)
f(3)


# program 3
# function as parameter to another 

sub = lambda x,y:x-y
def subtraction(fn,x,y):
    # fn = lambda x,y:x-y
    # x  = 40
    # y = 20
    e = fn(x,y)
    return e
e2 = subtraction(sub,40,20)
print(e2)



# program 4
mul = lambda x,y:x*y
def multiplication(fn,x,y):
    # fn = lambda x,y:x*y
    # x = 23
    # y = 2

    m = fn(x,y)
    return m
m2 = multiplication(mul,23,2)
print(m2)


# function as a return type 
def division():
    return lambda x,y:x/y

e = division()
#e  = lambda x,y:x/y
print(e)
print(e(12,4))



# function 
# program 1
# def - keyword
# add - function name 
# x,y - parameters
# return - keyword
#add(12,3) - call , 12,3 ===> arguments
# def add(x,y):
#     return x + y

# e = add(12,3)
# print(e)


# program 1
# def add(x,y):
#     return x + y

# add()
def add(x = 1,y = 3):
    return x + y

print(add())
print(add(1,22))
print(add(2))

# positional arguments 
def sub(x,y):
    return x - y
f = sub(y =3,x = 4)

# *args
from functools import reduce
def addition(*args):
    return reduce(lambda acc,el:acc+el,args)
f = addition(12,7,4,5,6,7,8)
print(f)


def additionE(*args):
    print(args)
    e = list(args)
    total = 0 
    for x in e:
        total = total + x
    return total
e = additionE(12,33,4,5,6)
print(e)


# program 5
# *kwargs
def addCity(**kwargs):
    print(kwargs)
    kwargs['city'] = "banglore"
    return kwargs

g = addCity(firstName = "subhuti" , lastName = "kapse", age = 21)
print(g)