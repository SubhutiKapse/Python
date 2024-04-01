names = ["subhuti","shruti","sanvi"]
names2 = names
names2[0] = "sapeksha"
print(names)
print(names2)

# program 2
# append()

fruits = ["apple","mango","banana"]
fruits.append("grapes")
print(fruits)


# program 3
# pop()
# pop(index)
# remove()

#                0            1           2       3
vegetables = ["cabbage","cauliflower","tomato","potato"]
# vegetables.pop()
# print(vegetables)
# vegetables.pop(1)
# print(vegetables)
vegetables.remove("tomato")
print(vegetables)
# append() , pop(index) or without index or remove()


# program 3
animals = ["tiger",'lion',"rabbit","panthar","tiger","lion"]
# animals.clear()
# print(animals)
q1  = animals.count('tiger')
print(q1)

# program 4
city = ["pune","mumbai","banglore","kolkata"]
city.reverse()
print(city)
# program 5
#             0         1            2      3
country = ["india","bangladesh","srilanka","japan"]
country.insert(2,"china")
print(country)

# program 6
district = ["chandrapur","wardha","nagpur"]
district.sort()
print(district)

# program 7 
listA = [11,22,33]
# listB = listA 
# listB[0] = 88
# print(listB)
# print(listA)

listD = listA.copy()
listD[1] = 111
print(listD)
print(listA)


listA =  [11,22,33]
listA.extend([77,88,99])
print(listA)
q1 = listA.index(77)
print(q1)


# program 1 
birthYear = [1989,1990,1991,1992]
ages = []
for x in birthYear:
    #print(2024- x)
    ages.append(2024 - x)
print(ages)

# program 2 
marks = [1,2,33,45,66,77,33,44,65]
above50 = []

for x in marks:
    if x> 50:
        above50.append(x)
print(above50)

#program 3
numbers = [11,22,33]
total  = 0 
for x in numbers:
    total = total + x
    #         0    +  11  -----> 11
    #         11   +   22 -----> 33
    #         33   +   33  -----> 66
print(total)
cities = ["pune","mumbai","banglore","chennai"]
for x in cities:
    print("welcome "+ x)