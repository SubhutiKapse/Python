# # #loops

# # #for loop


# # #program 1
# # #print 1 to 4
# # for x in range(1,5):
# #     print(x)

# # #program 2 
# # for x in range(4):
# #     print(x)

# # #program 3

# # #print hello 3 times
# # for x in range(3):
# #     print("hello")


# # #program 4
# # for x in range(1,6,2):
# #     print(x)
# # # #program 5
# # for x in range(0,10,2):
# #     print(x)

# #table of 2
# # #program 6
# #table of 2
# for x in range(2,22,2):
#     print(x)


# # #program 7
# #table of 5
# for x in range(5,55,5):
#     print(x)
# # #program 8
# #table of 10
# for x in range(10,110,10):
#     print(x)

# #break statement with loop
# for x in range(1,6):
#     if(x==3):
#         break
#     print(x)

# for x in range(5,0,-1):
#     if(x==3):
#         break
#     print(x)


# #continue
# for x in range(1,6):
#     if(x==3):
#         continue
#     print(x)


 #while loop
i1=1
while(i1<=5):
    print(i1)  
    i1=i1+1 

#while loop using break
i2=1
while(i2<=10):
    if(i2==5):
     break
    print(i2)
    i2=i2+1
#while loop using continue
i3=1
while(i3<=10):
    if(i3==5):
     break
    print(i3)
    i3=i3+1


    # program 1
# initialization 
#while(condition):
    # statements 
    # increment / decrement

# 
# program 1
i1 = 1
while(i1 <= 3):
    print(i1)
    i1 = i1 + 1 

# program 2
# print "hello" 3 times 
i2 = 1
while i2 <= 3:
    print("hello") 
    i2 = i2 + 1  

# program 3
# print 1 to 5
i3 = 1
while(i3 <= 5):
    print(i3)
    i3 = i3 + 1 

# program 4
# print 5 to 1
i4 = 5
while i4 >= 1:
    print(i4)
    i4 = i4 -1

#program 5
# table of 2 using while loop
i5 = 2
while i5 <= 20:
    print(i5)
    i5 = i5 + 2

#program 6
#table of 5 in reverse
i6 = 50
while i6 >= 5:
    print(i6) 
    i6 = i6 - 5 

# program 7
# break statement with while loop
i7 = 1
while i7  <= 5:
    if i7 == 3:
        break
    print(i7) 
    i7 = i7 + 1 

i7 = 1
while i7  <= 5:
    print(i7)  
    if i7 == 3:
        break
    i7 = i7 + 1  

i8 = 1
while i8 <= 5:
    if i8 == 3:
        i8 = i8 + 1  
        continue
    print(i8)  
    i8 = i8 + 1 



    # for loop
# for x in range(startValue,EndValue(not included),stepSize)
# startValue by default - 0
# stepsize by default -1 

# program 1
# print 1 to 3

for x in range(1,4):
    print(x)

for x in range(4):
    print(x)

# program 2
# print "hello"  3 times 
for x in range(3):
    print("hello")


# program 3
# print 1 to 5
for x in range(1,6):
    print(x)

# program 4
# print table of 2 
for x in range(1,6,2):
    print(x)

for x in range(2,21,2):
    print(x)

# program 5
# print 5 to 1
for x in range(5,0,-1):
    print(x)

for x in range(10,1,-1):
    print(x)

# table of 2 in reverse
for x in range(20,1,-2):
    print(x)

# table of 5 in reverse 
for x in range(50,4,-5):
    print(x)

# program 6
# break statement with for loop

for x in range(1,6):
    if x == 3:
        break
    print(x) 

for x in range(1,6): 
    print(x) 
    if x == 3:
        break

for x in range(5,0,-1):
    if x == 3:
        break
    print(x) 

for x in range(30,2,-3):
    if(x == 15):
        break
    print(x)

# continue statement with for 
for x in range(1,6): 
    if x == 3:
        continue
    print(x) 






