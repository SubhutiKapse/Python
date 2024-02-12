x=10
print(x)

x=120
print(x)


#arithmatic operators

q1=2
q2=4
print(q1+q2)
print(q1-q2)
print(q1*q2)
print(q1/q2)
print(q1%q2)


s1=3
s2=4
print(s1+s2)
print(s1-s2)
print(s1*s2)
print(s1/s2)
print(s1%s2)

def Calculator(x,y):
    print(x+y)
    print(x-y)
    print(x*y)
    print(x/y)
    print(x%y)

Calculator(2,4) 
Calculator(22,44) 

#function without parameter and without returntype
def addA():
    print(9+9)
addA()    

#function with parameter and without returntype
def addB(a,b):
    print(a+b)
addB(9,4)    


#function with parameter and with returntype
def addC(x,y):
    return x+y
a1=addC(2,4)
print(a1)

x=2
print(x)
print(type(x))

x=22.4
print(type(x))

x=True
print(type(x))

c="subhuti"
print(c)
print(type(c))


#comparision operator
print(3==3)
print(3>=3)
print(3<=3)
print(3!=3)
print(3==7)
print(3!=0)


#logical operator
#and

# true and true--->true
# true and false--->false
# false and true--->false
# false and false --->false

#or

# true or true--->true
# true or false--->true
# false or true--->true
# false or false --->false

#not

print( not 23==23)

#conditional statement

num =23
if num>1 and num==num:
  print("10 % discount")
if num>=21 and num<=34:
  print("20 % discount")
if num>11 and num==23:
  print("30 % discount")


  #loops
  h=[11,12,13,14,15]
  print(h)
  print(type(h))
  print(len(h))
  print(h[0])


names=["subhuti","shilpa","shruti","shivmala"]
print(type(names))  
print(names[1])
print(names[2])

for x in range(len(names)):
   print(x)
for x in range(len(names)):
      print(names)

city=["pune","mumbai","banglore","nagpur","hyderabad"]
print(city)
q1=len(city)
print(q1)


for x in city:
   print(x)


   
names=["manena","siddharth","shiva","vishal"]
q1=len(names)
print(q1)


w2=names
print(w2)

print(names)


fruits=["apple","banana","orange","chikoo"]
fruits[0]="grapes"
print(fruits)

print("orange" in fruits)




fruits=["apple","banana","orange","chikoo"]
fruits.append("straberry")
print(fruits)

x=23
print(x)
print(type(x))

#arithmetic operations
q1=23
q2=45
print(q1+q2)
print(q1-q2)
print(q1*q2)
print(q1/q2)
print(q1%q2)

#function without parameters and without returntype
def addA():
   print(9+9)
addA()   
#function with parameters and without returntype
def addB(x,y):
   print(x+y)
addB(7,9)   
#function with parameters and with returntype

def addC(x,y):
   return x+y
q1=addC(6,8)
print(q1)

#list

h1=[11,22,33,44,55]
print(h1)
print(type(h1))
print(h1[0])

for x in range(len(h1)):
   print(x)

for x in h1:
   print(h1[2])   

city=["nagpur","mumbai","pune","hyderabad"]
print(city)
print(type(city))
print(len(city))

q1=city
print(q1)


names=["subhuti","sapeksha","shruti","shivmala"]
(names[0])="shalakha"
print(names)

names=["subhuti","sapeksha","shruti","shivmala"]
names.append("kamla")
print(names)

q1=names.copy()
print(q1)

names.extend('pune')
print(names)

names.index("subhuti")
print(names)

names.insert(0,"pratishtha")
print(names)

names.sort()
print(names)

names.pop()
print(names)

names.reverse()
print(names)

listA=[11,22,33]
listB=listA
listB[0]=99
print(listA)
print(listB)

city=["nagpur","mumbai","pune","hyderabad"]
city2=city
city2[2]="pandharpur"
print(city2)
print(city2)

str="12345"
str.isalpha()
print(str)


names="subhuti"
names.capitalize()
print(names)

names.islower()
print(names)

names.isdigit()
print(names)

names=["subhuti","kapse",21,45]
print(names[0])
names.append("kamla")
print(names)
names[0]="chiryanka"
print(names)
names.pop()
print(names)


#dictionary

info={
   "first_name":"subhuti",
   "last_name":"kapse",
   "age":21,
   "rollno":4565
   }

for key in info.keys():
   print(key)

for pro in info.values():
   print(pro)   

for k,v in info.items():
   print(k,v)   


#conditional statement
   
num=75
if num>23 and num<90:
   print("10 % discount")
if num>23 and num<90:
   print("20 % discount")
if num>23 and num<90:
   print("30 % discount")

num=90
if num>23 and num<60:
   print("10 % discount")
elif num>23 and num<90:
   print("20 % discount")
elif num>23 :
   print("30 % discount")
else:
   print("incorrrect input")   



#elif 
   
numT=329

if numT> 21 and numT>=32:
   print("10 % discount")
elif numT> 21 and numT>=324:
   print("20 % discount")
elif numT> 22 and numT>=328:
   print("30 % discount")


   #if if
num=50
if numT> 21 and numT>=32:
   print("10 % discount")
if numT> 21 and numT>=32:
   print("20 % discount")
if numT> 21 and numT>=32:
   print("30 % discount")   




marks=183
if num>278 and num>398:
   print("grade A")
elif num>243 and num>783:
   print("grade B")
elif num>276 and num>398:
   print("grade C")
else:
   print("fail....!")


#program 4
   x1=35
   x2=30
   x3=489


if x1>x2 and x1>x3:
   print("x1 is greater")
elif x2>x1 and x2>x3:
   print("x2 is greater")
else:
   print("x3 is greater")   
   


#if if
num=23   

if num>3 and num>21:
 print("10 % discount")
if num>3 and num>21:
 print("20 % discount")
if num>3 and num>21:
 print("30 % discount")


info={
  "first_name":"subhuti",
  "last_name":"kapse",
  "age":21,
  "rollno":345
}
#retrive
print(info['first_name'])
#update
info['first_name']="sapeksha"
print(info)
#delete
info.pop("age")
print(info)
#add
info['city']="pune"
print(info)


vehicle={
   "color":"black",
   "type":"mercedes benz",
   "regno":124
   }
   

#retrive

print(vehicle['color'])
#add
vehicle['average']="5500"
print(vehicle)
#delete
vehicle.pop("regno")
print(vehicle)

#update 
vehicle['city']="banglore"
print(vehicle)

print("color" in vehicle)


info={
  "first_name":"subhuti",
  "last_name":"kapse",
  "age":21,
  "rollno":345
}
info2=info
info2['age']=56
print(info)
print(info2)

for x in info:
   print(info[x])


for k in info.keys():
   print(k)   

for v in info.values():
   print(v)   

for k,v in info.items():
   print(k,v)   

q1= dict.fromkeys(["subhuti","chavi","kamla","nisarga"])
print(q1)