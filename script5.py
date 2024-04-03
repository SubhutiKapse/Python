# loop 
#for x in range(startIndex, endIndex(not included),stepSize):
    # statements
# for x in range(1,5):
#     print(x)

# for x in range(6):
#     print(x)

# for x in range(2,21,2):
#     print(x)

# for x in range(50,4,-5):
#     print(x)

# for x in range(1,6): # 2 # 3
#     if x == 3:
#         break 
#     print(x) # 1 # 2

# for x in range(5,1,-1): 
#     print(x)
#     if x == 3:
#         break 

# for x in range(1,6):# 2 # 3 # 4 # 5 
#     if x == 3:
#         continue
#     print(x) # 1 # 2 #4 # 5


# while loop
# intialization 
# while(condition):
    # statement
    # increment

# program 1
# print 1 to 3

t1 = 1
while(t1 <= 3):
    print(t1) # 1 #2 #3
    t1 = t1 + 1 #2 #3 #4

# program 2 print 1 to 5 
t2 = 1
while(t2 <= 5):
    print(t2)
    t2 = t2 + 1

# program 3 table of 2 
t3 = 2
while t3 <= 20:
    print(t3)
    t3 = t3 + 2

# program 5 table of 5
t4 = 50
while t4 >= 5:
    print(t4)
    t4 = t4 - 5 

# program 6 break statement with while loop
t5 = 1 
while t5 <= 5:
    if t5 == 3:
        break
    print(t5) # 1 # 2
    t5 = t5 + 1 # 2 # 3

# program 7
t6 = 5
while t6 >= 1:
    print(t6) # 5 # 4 # 3
    if t6 == 3:
        break
    t6 = t6 - 1 # 4 # 3

# program 8 while loop with continue 
t7 = 1
while t7 <= 5:
    if t7 == 3:
        t7 = t7 + 1 # 4
        continue
    print(t7)   # 1 # 2 # 4 # 5
    t7 = t7 + 1   # 2 # 3 # 5 