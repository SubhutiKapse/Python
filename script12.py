#program 1
first_name="subhuti",
last_name="kapse",
middle_name="""
ajay
"""

info='''
i am learning
'''
print(type(info))

#program 2
city="chandrapur"
print(city[1::])
print(city[1:5:])
print(city[1::-1])
print(city[1:-1:])

#program 3
city1="pune"

print(city1[0])
print(city1[1])
print(city1[2])
print(city1[3])

for x in range(4):
    #print(x)
    print(city1[x])

    # program1 

first_name = 'chinmay'
last_name = "deshpande"
middle_name = """
shrish
"""
info = '''
    i am learning
'''
print(type(info))


# program 2
#   0     1     2     3     4     5     6     7    8    9
#   c     h     a     n     d     r     a     p    u     r 
#  -10   -9    -8    -7    -6    -5    -4    -3   -2   -1

city = "chandrapur"
#print(city[startIndex:EndIndex(not included):stepSize])
print(city[1::])
print(city[2:7:])
print(city[-8:])
print(city[-8:-2])
print(city[1:-1:])
print(city[0:10:2])
print(city[-1:-3])

# program 3

city3 = "pune"

# 0  1  2  3
# p  u  n  e
print(city3[0])
print(city3[1])
print(city3[2])
print(city3[3])

for x in range(4):
    #print(x)
    print(city3[x])

for x in range(len(city3)-1,-1,-1):
    #print(x)
    print(city3[x])

for x in range(50,4,-5):
    print(x)

city4 = "nagpur"

for x in range(len(city4)):
    #print(x)
    print(city4[x])

for char in city4:
    print(char)


# program 4    
print("ti" in "subhuti")

 
# program5
city5 = "wardha"
# 0  1  2  3  4  5 
# w  a  r  d  h  a

i1 = 0
while(i1 < len(city5)):
    #print(i1)
    print(city5[i1])
    i1 = i1 + 1

i2 = len(city5) -1
while(i2 >= 0):
    print(city5[i2])
    i2 = i2 - 1