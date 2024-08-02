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






