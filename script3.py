# loops ??
# while and for loop

#  for 
# range()

#for x in range(startIndex,EndIndex(not included),stepSize):
    # statements

# print 0 to 9
for x in range(10):  # if startIndex not mentioned , zero is deafault
    print(x)

# print 2 to 9 
for x in range(2,10):
    print(x)

# print 1 to 5
for x in range(1,6):
    print(x)

# table of two 
# 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
for x in range(2,21,2):
    print(x)


# table of three
for x in range(3,31,3):
    print(x)

# table of five in reverse
for x in range(50,4,-5):
    print(x)

# table of 10 in reverse 
for x in range(100,9,-10):
    print(x)
    
# break statement with for loop
for x in range(1,6):  # 2 #3
    if x == 3:
        break
    print(x)#1 #2

for x in range(1,6):  # 2 # 3
    print(x) # 1 # 2 # 3
    if x == 3:
        break 
    