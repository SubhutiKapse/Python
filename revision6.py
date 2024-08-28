#list methods
animals=["tiger","lion","deer","monkey","rabbit","tiger"]
q=animals.append("giraffe")
print(animals)
print(q)
no=[11,22,33,44,11,31,11,43]
q1=no.count(11)
print(q1)

no.clear()
print(no)

names=["subhuti","shruti","manika","shyli"]
names.extend("rama")
print(names)

names.insert(0,"kamla")
print(names)

names.pop(1)
print(names)

names.reverse()
print(names)

names.remove("shyli")
print(names)

# q1=names.index("manika")
# print(q1)

q1=names.copy()
print(q1)

names.extend("manvika")
print(names)

listA=[11,12,13]
listB=listA
listB[0]=65
print(listA)
print(listB)

city=["nagpur","pune","mumbai","hyderabad"]
city2=city.copy()
city[1]="surat"
print(city)
print(city2)



#string
greet= "hello"
greet2='hi'
print(greet)

for x in range(len(greet)):
    print(x)


for x in greet:
    print(greet)    
#string methods
first_name="subhuti"
q1=first_name.upper()
print(q1)


q1=first_name.lower()
print(q1)

q1=first_name.capitalize()
print(q1)

q1=first_name.isupper()
print(q1)

q1=first_name.islower()
print(q1)


q1=first_name.startswith('s')
print(q1)

q1=first_name.endswith('i')
print(q1)

#dictonary 

info=["subhuti","kapse",21,45]
#retrive
print(info[0])
#update
info[0]="sapeksha"
print(info)
#delete
info.remove("kapse")
print(info)
#add
info.append("pune")
print(info)



name=["subhuti","kapse",21,56]
#retrive
print(name[0])
#update
name[0]="sapeksha"
#print(names)
#delete
name.remove("kapse")
print(name)
#add
name.append("pune")
print(name)

#program 2
info={
    "first_name":"subhuti",
    "last_name":"kapse",
    "age":21,
    "rollno":1116
}

print(info)
print(type(info))
print(info["first_name"])


print(info['first_name'])

#info['last_name']="shanu"

info['city']="pune"
print(info)

info['city']="mumbai"
print(info)

info.pop("age")
print(info)

info.popitem()
print(info)

vehicle={
    "color":"red",
    "type":"rangerover"
}
#retrive
print(vehicle['color'])
#update
vehicle['type']="mercedes benz"
print(vehicle)
#delete
vehicle.pop('type')
#print(vehicle)
#add
vehicle['reg no']=124
print(vehicle)

for x in vehicle:
    print(x)


subject={
    "subOne":"english",
    "subtwo":"hindi",
    "subthree":"marathi",
    "subfour":"sanskrit",
}    

for key in subject.keys():
    print(key)

for val in subject.values():
    print(val)    

for k,v in subject.items():
    print(k,v)    

#tuple vs list
listname=["subhuti","kamla","jamla","vimla"]
print(listname)        
print(type(listname))
print(len(listname))

listname.append("sapeksha")
print(listname)

listname[0]="shanu"
print(listname)

listname2=("zimba","sikandar","fatima","shibra")
print(listname2)

#using range
for x in range(len(listname2)):
    print(x)

for x in range(len(listname2)):
    print(listname2[x])

#without range
for item in listname2:
    print(item)        


#program 
    
tupleD =(11,22,33,11,44,55,11)
q = tupleD.count(11)    
print(q)

w2=tupleD.index(22)
print(w2)











x=10
print(x)

x=34
print(x)

#arithmetic operation
a=10
b=15
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)

#function without parameters and without returntype
def addA():
    print(9+9)

addA()    
addA()

#function with parameters and without returntype
def addB(x,y):
    print(x+y)
addB(2,4)
addB(1,3)    

#function with parameters and without returntype
def addC(x,y):
    return x+y
q1=addC(2,4)
print(q1)

#conditional statement

#if statement
num=20
if 5<=num and 11<num:
    print("10% discount")
if 20<=num and 14<num:
    print("20% discount")
if 15<=num and 11<num:
    print("30% discount")



num=20

if 5<=num and 11<num:
    print("10% discount")
elif 20<=num and 14<num:
    print("20% discount")
elif 15<=num and 11<num:
    print("30% discount")

#loops
#while and for loop
    #with range
    #print 0 to 9
for x in range(10):
        print(x)

#print 1 to 6
for x in range(1,6):
    print(x)        


#print -6 ti -1
for x in range(-6,-1):
    print(x)    

#print table of 2
    for x in range(2,21,2):
        print(x)

#table of 5
        for x in range(5,51,5):
            print(x)        

for x in range(50,4,-5):
    print(x)            

#continue with for loop
for x in range(1,6):
    if x==3:
        continue
    print(x)

#break
for x in range(1,8):
    if x==4:
        continue
    print(x)    

for x in range(1,6):
    print(x)
    if x==3:
      break


#continue 
    #break


for x in range(1,8):
    if x==4:
        continue
    print(x)    


for x in range(1,8):
    print(x)
    if x==4:
        print(x)    

#while 
        t1=1
while (t1<=3):
    print(t1)
    t1=t1+1                


y1=1
while(y1<=5):
    print(y1) 
    y1=y1+1  


#table of 2    
t1=1
while(t1<=20):
    print(t1)
    t1=t1+1

#list
    names=["subhuti","sapi","sapeksha","shilpa"]
    print(names)        
names[2]="mayuri"
print(names)

print(type(names))
(print(len(names)))
print(names[0])

# for x in range(len(names)):
#     print(names[x])

for subhuti in names:
    print(subhuti)    

names=["subhuti","sapi","sapeksha","shilpa"]
i=0
while(i<=3):
    print(names[i])
    i=i+1   


print("subhuti" in names)    

names=["subhuti","sapi","sapeksha","shilpa"]
names[0]="komal"
print(names)
names.append("pushpa")
print(names)

names.pop()
print(names)

names.remove("sapi")
print(names)

names.pop(0)
print(names)

listA=[11,22,33]
listB=listA
listB[0]=66
print(listA)
print(listB)


listQ=listA.copy()
listQ[1]=111
print(listQ)
print(listA)


info={
    "firstName":"subhuti",
    "lastName":"kapse",
    "age":21,
    "rollno":9879
}
print(info['firstName'])
info['firstName']="poorva"
print(info)
info['city']="pune"
print(info)

info.pop('age')
print(info)

for key in info.keys():
    print(key)

for val in info.values():
    print(val)    

for k,v in info.items():
    print(k,v)    

#print 0 to 9
    for x in range(10):
        print(x)    

#print 2 to 9
        for x in range(2,10):
            print(x)

#print 1 to 5
# for x in range(1,6):
#             print(x)            


# for x in range(1,10):
#     if x==2:
#         break
#         print(x)

# #continue with for loop
# for x in range(1,6):
#     if x==2:
#      break:
#       print(x)        











################################
# x=10
# print(x)

# #arithmetic operation
# a=5
# b=3
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)


# #function without parameters and without returntype
# def add():
#     print(9+9)

# add()
# add()    
# #function with parameters and without returntype
# def sub(x,y):
#     print(x-y)

# sub(2,8)
# sub(9,7)    

# #function with parameters and with returntype
# def addA(u,v):
#     return u+v
# s1=addA(7,7)
# print(s1)

# #loops
# #for loops using range
# #print 1 to 10
# for x in range(11):
#     print(x)
# #print 10 to 1
#     for x1 in range(10):
#         print(x1)
# #print table of 2
#     for x in range(2,21,2):
#         print(x)
# #print table of 10
#     for x in range(10,101,10):
#         print(x)

#  #print table of 3
#         for x in range(3,31,3):
#             print(x)      

# #print reverse table of 3
#         for x in range(30,0,-3):
#             print(x)

# #print reverse table of 10
#             for x in range(100,9,-10):
#                 print(x)


# #break statement with for loops
# for x in range(1,6):
#     print(x)#1#2#
#     if x==3:
#      break

# for x in range(1,9):
#    if x==5:
#     break
# print(x)     

# for x in range(1,8):
#   print(x)
#   if x==4:
#     break
  
# for x in range(1,6):
#   if x==4:
#     break
#   print(x)  

# #continue with loops
#   for x in range(1,5):
#     if x==3:
      
#       continue
# print(x)


# #break
# for x in range(1,5):
#   if x==3:
#     break
#   print(x)

#   for x in range(1,10):
#     print(x)
#     if x==5:
#       break

# #continue
#     for x in range(1,8):
      
#       if x==6:
#         continue
#       print(x)


#       for x in range(1,7) :
        
#         if x==4:
#           continue   
#         print(x)


#  #while loops
# q1=1
# while(q1<=4):
#   print(q1)
#   q1=q1+1         

# #table of 2
#   q2=2
#   while(q2<=20):
#     print(q2)
#     q2=q2+2


# #table of 5
# q3=5
# while(q3<=50):
#   print(q3)
#   q3=q3+5        


# #table of 5 in reverse
#   w1=50
# while(w1>=5):
#  
#   #w1=w1+5 

# #   s1=2
# #   while s1<=20:
    
# #     if s1==5:
# #       break
# #     print(s1)
# #     s1=s1+2
  
# #list
# names=["subhuti","sapeksha","shivani","shyli"]
# print(names)
# print(type(names))
# print(len(names))

# names[0]
# print(names)
# names[1]
# print(names)
# names[2]
# print(names)
# names[3]
# print(names)

# names[0]="kamla"
# print(names)
# names[1]="shamli"
# print(names)
# for x in range(len(names)):
#  print(x)

# for  item in names:
#  print(item) 

# q1=0
# while(q1<len(names)):
#  print(q1)
# #  print(names[q1])
# #  q1=q1+1 

# # flowers=["rose","mogra","jasmine","tulip","lily"]
# # print(flowers)
# # print(type(flowers))
# # print(len(flowers))
# # print("lily" in flowers)

# # a1=1
# # while(a1<=5):
# #  if a1==3:
# #   a1=a1+1
# #   print(a1)

# #function without parameters and without returntype
# def addA():
#  print(2+3)
# addA()
# addA() 

# #function with parameters and without returntype

# def addB(x,y):
#  print(x+y)
# addB(2,4) 

# #function with parameters and with returntype
# def addC(x,y):
#  return x+y
# q1=addC(12,3)
# print(q1)


# #conditional statement
# num=10
# if (num<=20 and num<=30):
#  print("10 % discount")
# if (num<=20 and num<=30):
#  print("20 % discount")
# if (num<=20 and num<=30):
#  print("30 % discount")


#  numT=20
# if (num<=20 and num<=30):
#  print("10 % discount")
# elif (num<=20 and num<=30):
#  print("20 % discount")
# elif (num<=20 and num<=30):
#  print("30 % discount")
# # else:
# #  print("no discount")


#int as parameter and int as returntype
def add(x,y):
 return x+y
q1=add(1,3)
print(q1)

#float as parameter and float as returntype

#string as parameter and string as returntype
#boolean as parameter and boolean as returntype
#list as parameter and list as returntype

#tuple as parameter and tuple as returntype

#dictionary as parameter and dictionary as returntype
#set as parameter and set as returntype




#instance
#static
#class

class PersonA:
 country="india"
 def __init__(self,fn,ln,ag):
  self.firstName=fn
  self.lastName=ln
  self.age=ag

def displayName(self):
 print(self.firstName + self.lastName)

def changeCountry(cls,cn):
 cls.country="bharat"

subhuti=PersonA("subhuti","kapse",21)
print(subhuti.firstName)
print(subhuti.lastName)
print(subhuti.age)
#subhuti.displayName()



class PersonB():
 country="india"
 def __init__(self,fn,ln,ag):
  self.firstName=fn
  self.lastName=ln
  self.age=ag

def displayName(self):
 print(self.firstName + self.lastName)


def changeCountry(cls,cn):
 cls.country="bharatmata"
sanvi=PersonB("sanvi","rai",22)

print(subhuti.firstName)
print(subhuti.lastName)
print(subhuti.age)
print(subhuti.country)