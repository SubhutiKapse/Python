#function

#int as parameter and int as return
def add(x,y):
    return x+y
r=add(3,2)
print(type(r))


#float as parameter and float as return
def add(x,y):
    return x+y
q=add(3.1,2.1)
print(type(q))


#string parameter and string as return
def greet(word):
    return "hello"+word
w=greet("subhuti")
print(type(w))


#list parameter and list as return
fruits=["apple","banana","orange","grapes"]
def addfruits(lst):
    fruits.append("straberry")
    return lst
h=addfruits(fruits)
print(type(h))


#dict parameter and dict as return
info = {
    "firstName":"subhuti",
    "lastName":"kapse"
}
def addLang(dictB):
    dictB['language']="english"
    return dictB
l=addLang(info)
print(l)
print(type(l))


#tuple parameter and tuple as return
q1= 11,12
q1=(11,12)
def addElementToTuple(tupA):
    tupA=list(tupA)
    print(tupA)
    tupA=tuple(tupA)
    return tupA
l=addElementToTuple(q1)
print(type(l))


#set parameter and set as return
setA={11,22,33}
def addEtoS(n):
    setA.add(n)
    return setA
l=addEtoS(44)
print(type(l))