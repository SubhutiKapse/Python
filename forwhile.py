#loops
#for and while loops

#for loops in range()
#range(startIndex,endIndex(not included)),steps)
#default----0 as startindex


#program 1
for x in range(5): #starts with 0 and ends with 4
    print(x)

#program 2
for x in range(1,10):
    print(x)        #starts with one and ends with nine

#program 3 #table of 2
for x in range(2,21,2):
    print(x)    

#program 4 
    for x in range(1,11) :
        print(x)   

#program 5 reverse of table 5
for x in range(50,4,-5):
    print(x)               


#program 6  reverse table of 3
for x in range(30,2,-3):
    print(x)    


#program 7
for x in range(1,10):
    
    if x==3:
     break   
    print(x) 

#program 8
for x in range(30,2,-3):
     print(x) #if we write print 1st then the if conditions prints upto the value
     if x==3:
         break
     

#program 9
#continue with for loop

for x in range(1,6):
    if x==3:
        continue
    print(x)    

#program 10
    for x  in range(6,1,-1):
        if x==3:
            continue
        print(x)               


#while loop
        #initialization
        #whilw(condiotion):
        #statement
        #increment    

#program 1
        #print 1 to 3


t1=1
while(t1 <=3) :
    print(t1)
    t1=t1+1


#program 2 print 1 to 5
    t2=1
    while(t2 <= 5):
        print(t2)
        t2=t2+1
    
#program 3 print table of 5
        
t3=5
while(t3<=50):
    print(t3)
    t3=t3+2
      

#program 4 reverse table of 5
    t4=50
    while(t4>=5):
        print(t4)
        t4=t4-5      


##program 5 table of 6
t5=6
while(t5<=60):
    print(t5)
    t5=t5+6

#program 6 table of 10
    
t6=10
while (t6<=100):
    print(t6)
    t6=t6+10      
    
n=10
while n<=100:
    print(n)
    n=n+10

#print reverse of table 10
f1=100
while(f1>=10):
    print(f1)
    f1=f1-10


#print table of 23
s1=23
while(s1<=230):
    print(s1)
    s1=s1+23


for x in range(1,5):
    print(x)

for x in range(1,5,2):#2 element skip karega
    print(x)    

for x in range(2,21,2):
    print(x)    

for x in range(50,1,-1):
    print(x)    


for x in range(100,10,10):
    print(x)    

for x in range(1,6):#2 #3
    if x==3:
      break
    print(x)#1 #2 #3


for x in range(5,1,-1):
 print(x)
 if x==3:
     break
 
 #statement with continue
 for x in range(1,6):
     if x==4:
         continue
     print(x)

