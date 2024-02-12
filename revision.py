



# 10 pairs 50 lines of code
def Calculator(c,u):
  print(c+u)
  print(c-u)
  print(c*u)
  print(c/u)
  print(c%u)   
 
Calculator(3,5) 
Calculator(2,1)

#function without parameters
def addA():
  print(2+4)
addA()
addA()
addA() 

#function with parameters and without return type
def AddA(x,y):
 print(x+y)
  
AddA(4,5)
AddA(4,23)
AddA(4,55)
AddA(4,52)
 

#function with parameters and with return type
def addC(c,u):
  return c+u
r= addC(4,5)   
print(r)
print(r+r)

#conditional statements
#if condition
num=20
if num<=30 and num >10:
 print("10 % discount")
if num <39 and num >=20:
 print("20 % discount")   
if num >2 and num==20:
  print ("30 % discount") 

  #program 3
  num=20
if num<=30 and num >10:
 print("10 % discount")
elif num <39 and num >=20:
 print("20 % discount")   
elif num >2 and num==20:
  print ("30 % discount")

  

#list
  
names=["ram","lakhan","satish","kamlesh"]
print(names)
print(type(names))

# program 3
q1=len(names)
print(q1)

#program 4
fruits=["grapes","banana","orange","mango"]
fruits[0]="apple"
print(fruits)

names =["suhuti","shruti","shrutika","shivmala"]
print(names[1])

names[0]="ishita"
print(names)

# print names
names =["suhuti","shruti","shrutika","shivmala"]
print(names[1::])
print(names[1:2:])
print(names[1:len(names)])

# print numbers


numbers =[11,22,33,44,55,66]
print(numbers)
print(numbers[len(numbers)-1::-1])
print(numbers[5])
print()

# program 7 

countries = ["india","bangladesh","pakisthan","neynmar"]
print(countries)
print(countries[3])
print(countries[len(countries) -1::1])
print(countries)

countries = ["india","bangladesh","pakisthan","neynmar"]
print(countries)
print(countries[3])
print(countries[len(countries) -1::-1])
print(countries)
# program  8

marks =[11,22,33,44,55,66]
for c in range(len(marks)):
  print(marks[c])

  #
  n =[111,2222,33333,444444,5555555]
  for v in range(len(n)):
    print(n[v])

#list is used when we have to store more than one value
    #methods

names=["ram","lakhan","satish","kamlesh"]
names.append("raman")
print(names)

#



#names.clear()
print(names)

names.extend(["shila"])
print(names)

a =names.index("kamlesh")
print(a)

names.insert(2,"tinku")
print(names)

names.pop()
print(names)

names.remove("ram")
print(names)

names.reverse()
print(names)





names.sort()
print(names)

cities =["pune","mumbai","nagpur"]

city2=cities.copy()
city[1]="surat"

# 
listA =[11,22,33,44,55]
print(listA[0])
print(listA)




