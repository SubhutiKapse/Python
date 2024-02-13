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