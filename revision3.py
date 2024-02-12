x=10
print(x)
print(type(x))


y=12.4
print(y)
print(type(y))

z= True
print(z)
print(type(z))

a= "subhuti"
print(a)
print(type(a))

s=[11,34,45,56] 
print(s)
print(type(s))

#conditional statement

num=20
if num<=50 and num>9:
 print("10%")
if num>0 and num > 3: 
  print("20%")
if num>10 :
  print("30%")

  num=20
if num>50 and num<9:
 print("10%")
elif num>200 and num < 3: 
  print("20%")
elif num>30:
  print("30%")
else:
  print("incorrect")

  #
  x1=10
  x2=22
  x3=5

if x1 < x2 and x1 > x3:
  print("x1 is greater")
elif x2 > x1 and x2 > x3 :
 print("x2 is greater")
else:
 print("x3 is greater")



x=10
print(x)


h= [22,34,45,67,78]
print(h)
print(type(h))
print(len(h))
print(h[0])
print(h[4])

#program 2
names =["subhuri","shruti","shivmala","sugrata"]
print(names[0])

for x in range(len(names)):
  print(x)

for x in names:
  print(x)  


cities=["nagpur","pune","hydrabad","banglore"]
print(cities)  
w1=len(cities)
print(w1)

names =["subhuri","shruti","shivmala","sugrata"]
print("subhuri" in names)
if("subhuti"in names):
 print("subhuri is active")
else:
  print("subhuri is inactive")

  #list

  names =["subhuri","shruti","shivmala","sugrata"]
  w2=len(names)
  print(w2)
  names[3]="kamlesh"
  print(names)
  print("shruti" in names)
  


def add(x,y):
  return "hello"
q= add(2,3)
print(q)

#program 2
names=["subhuti","shruti","shivmala","sugrata"]
print(type(names))
print(len(names))
q=len(names)
print(q)


#program 2
names=["subhuti","shruti","shivmala","sugrata","subhuti"]
q=names.append("ram")
print(names)
print(q)

w=names.clear()
print(w)


num=[11,22,33,44,55,66,11,77,88,11]
r=num.count(11)
print(r)


fruits=["apple","banana","orange","mango"]
fruits.insert(1,"chikoo")
print(fruits)



fruits.extend(["kivi","chikoo"])
print(fruits)

fruits.pop()
print(fruits)


q1=fruits.index("apple")
print(q1)

fruits.extend(["chickoo","grapes"])
print(fruits)


listA=[11,22,33]
listB=[44,55,66]
listB.extend(listA)
print(listA)
print(listB)

animals=["tiger","lion","rabbit",]

animals.sort()
print(animals)

animals.reverse()
print(animals)


city =["pune","mumbai","hyderabad","nagpur"]
city2=city.copy()
city[1]="surat"
print(city)
print(city2)


x=23
print(x)

y=34
print(y)
print(type(y))


#arithmetic operation

a=5
b=3

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)

n=7
m=2
print(n+m)
print(n-m)
print(n*m)
print(n/m)
print(n%m)

 
def cal(n,m):
 print(n+m)
 print(n-m)
 print(n*m)
 print(n/m)
 print(n%m)

cal(5,8)
#function without parameters and with return type
def addA():
  print(9+9)
  
  addA()
  addA()
  addA()
  addA()

  #function with parameter and with returntype
def addC(x,y):
  print(x+y)
addC(2,4)  

#function with parameter and return value

def addC(x,y):
  return x+y
q1= addC(2,4)
print(q1)




