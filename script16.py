#int as parameter and as returntype
def addOne(x,y):
    return x+y
q1=addOne(2,4)
print(q1)
#float as parameter and as returntype
def addTwo(x,y):
    return x+y
q2=addTwo(1.2,4.3)
print(q2)

def addThree(x,y):
    return x-y
q3=addThree(3.2,4.1)
print(q3)
#boolean as parameter and as returntype
# def canDrive(age,haveVehicle):
#     if age > 18 and haveVehicle:
#         return True
#     else:
#         return False
#     w = canDrive(19,True)
#     print(w)
#string as parameter and as returntype
def greet(name):
    return("welcome "+name)
a=greet("subhuti !")
print(a)
#list as parameter and as returntype
names=["subhuti","sapeksha","shyli","shamli"]
def addNames(lst):
    lst.append("vijeet")
    return lst
p=addNames(names)
print(p)
#dictionary as parameter and as returntype
info={
    "firstName":"subhuti",
    "lastName":"kapse"
    #city:banglore

}
def addCity(information):
    information['city']="banglore"
    return information
u=addCity(info)
print(u)
#tuple as parameter and as returntype
numbers=(11,22,33)
#(11,22,33)
def addValue(tupA):
    tupA=list(tupA)
    tupA.append(99)
    tupA=tuple(tupA)
    return tupA
a1=addValue(numbers)
print(a1)

#set as parameter and as returntype
setA={11,22,33}
def addElement(seta):
    seta.add(66)
    return seta
x=addElement(setA)
print(x)