#TUPLE

#tuple stores the value by index

tupleA = (11,22,33)
#tupleA[0] = 44
print(tupleA)
print(type(tupleA))




tupleB = 11,12,13
print(type(tupleB))
print(tupleB)

# how to find a particular element is available on tuple
print(12 in tupleB)
print('13' in tupleB)

# loop through tuple using range 
#            0          1        2        3
tupleC = ("subhuti","shruti","sanvi","sayu")
print(tupleC)
for x in range(len(tupleC)):
    #print(x)
    print(tupleC[x])

# loop through tuple without range 
for item in tupleC:
    print(item)

# loop through tuple with while loop
i1 = 0 
while i1 < len(tupleC):
    #print(i1)
    print(tupleC[i1])
    i1 = i1 + 1

# how to add element in tuple 
#            0        1       2         3
fruits  = ["apple","mango","banana","oranges"]
print(fruits)
print(len(fruits))
fruits.append("grapes")
print(fruits)

fruits  = ("apple","mango","banana","oranges")
fruits = list(fruits)
fruits.append("grapes")
fruits = tuple(fruits)
print(fruits)


def returnTuple():
    return 12,

a = returnTuple()
print(a)

tupleD = ("apple","mango","banana","apple","apple")
print(tupleD)
q1 = tupleD.index("apple")
print(q1)

q2 = tupleD.count("apple")
print(q2)

tupleD = ("apple","mango","banana","apple","apple")
tupleD = list(tupleD) # tuple to list
tupleD.remove("mango") # removing mango
tupleD = tuple(tupleD) #tuple
print(tupleD)


tupleA = (11,22,33)
#tupleA[0] = 44
print(tupleA)
print(type(tupleA))


# Does tuple stores the value by index ??
#yes

tupleB = 11,12,13
print(type(tupleB))
print(tupleB)

# how to find a particular element is available on tuple
print(12 in tupleB)
print('13' in tupleB)

# loop through tuple using range 
#            0          1        2        3
tupleC = ("subhuti","shruti","sani","sanvi")
print(tupleC)
for x in range(len(tupleC)):
    #print(x)
    print(tupleC[x])

# loop through tuple without range 
for item in tupleC:
    print(item)

# loop through tuple with while loop
i1 = 0 
while i1 < len(tupleC):
    #print(i1)
    print(tupleC[i1])
    i1 = i1 + 1

# how to add element in tuple 
#            0        1       2         3
fruits  = ["apple","mango","banana","oranges"]
print(fruits)
print(len(fruits))
fruits.append("grapes")
print(fruits)

fruits  = ("apple","mango","banana","oranges")
fruits = list(fruits)
fruits.append("grapes")
fruits = tuple(fruits)
print(fruits)


def returnTuple():
    return 12,

a = returnTuple()
print(a)

tupleD = ("apple","mango","banana","apple","apple")
print(tupleD)
q1 = tupleD.index("apple")
print(q1)

q2 = tupleD.count("apple")
print(q2)

tupleD = ("apple","mango","banana","apple","apple")
tupleD = list(tupleD) # tuple to list
tupleD.remove("mango") # removing mango
tupleD = tuple(tupleD) #tuple
print(tupleD)