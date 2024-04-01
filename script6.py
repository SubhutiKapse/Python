x = 10 
print(x)

# list 
#            0         1        2       3
names = ["subhuti","shruti","shyli","sanvi"]
print(names)
names[2] = "sapeksha"
# list stores the value by index

city = ["pune","banglore","kolkata","chennai"]
print(city[0])

# number of element in list
fruits = ["apple","mango","banana","grapes"]
print(len(fruits))
print(len(fruits))

# program2
# how to update the value in list
animals = ["tiger","lion","cat","rabbit","panthar"]
animals[0] = "snake"
print(animals)

# program3
#             0       1       2       3         4
country  = ["india","cuba","china","srilanka","italy"]

# for loop
# for loop with range()
# while loop

for x in range(5):
    #print(x)
    print(country[x])

# x = 0
# x = 1
# x = 2
# x = 3
# x = 4

#             0       1       2        3         4
country  = ["india","cuba","china","srilanka","italy"]
for x in range(len(country)-1,-1,-1):
    #print(x)
    print(country[x])



# program 4
#         0        1          2         3
city = ["pune","banglore","kolkata","mysore"]
for item in city:
    print(item)
    

# program 5
# while loop
#             0        1       2         3
flowers  = ["lily","jasmine","rose","sunflower"]
#print(flowers)
i1 = 0
while(i1 < len(flowers)):
    #print(i1)
    print(flowers[i1])
    i1 = i1 + 1

i2 = len(flowers) - 1
while(i2 >= 0):
    print(i2)
    print(flowers[i2])
    i2 = i2 -1 

# any element present in list ??
#           0        1       2         3       4
names = ["ram","sham","","jay",'veeru']
print("ram" in names)