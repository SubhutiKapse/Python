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
for x in range(1,6):
            print(x)            


for x in range(1,10):
    if x==2:
        break
        print(x)

#continue with for loop
    for x in range(1,6):
    if x==2:
    break:
print(x)        