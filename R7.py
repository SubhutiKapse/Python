# #STRING
# #string stores the value by index
# subject="English"
# print(subject[0])



# #for loop
# for char in subject:
#     print(char)


# #with range
# for x in range(len(subject)):
#     #print(x)
#     print(subject[x])

# #while loop

# q1=0
# while(q1<len(subject)):
#     print(q1)
#     print


x=7
print(x)
print(type(x))

y=10.8
print(y)
print(type(y))

z=True
print(z)
print(type(z))

a="subhuti"
print(a)
print(type(a))

fruits = ["apple","mango","grapes","papaya"]
print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])


#          0
cities = ['pune',"nagpur","bangalore","kolkata"]
#                                       -1
print(cities[-1])
print(cities[-2])


country = ["india","pakistan","bangladesh","srilanka","china"]
print(len(country))

#with range
for x in range(5):
    print(country[x])

state = ["MH","MP","UP","RJ"]
for x in range(len(state)):
    print(state[x])


#without range
for x in state:
    print(x)

#loop over list- while loop
animals = ["tiger","lion","rabbit","snake"]
i1 = 0
while(i1 < len(animals)):
    #print(i1)
    print(animals[i1])
    i1 = i1 + 1


#LIST METHODS




# list tuple dictionary ,sets,string -- CRUD , methods , loop

cities = ["pune","mumbai","bangalore","kolkata"]

# verify whether a  particular element is present in list 
print("pune" in cities)

# methods in list
vegetables = ["tomato",'potato','brinjal',"cauliflower"]
vegetables.append("ladyfinger")
print(vegetables)

# program 2 pop - index
#['tomato', 'potato', 'brinjal', 'cauliflower', 'ladyfinger']
vegetables.pop()
print(vegetables)
# passing index to pop
vegetables.pop(2)
print(vegetables)

# program 3
countries = ["india","pakistan","bangladesh","srilanka"] 
countries.remove("pakistan")
print(countries)

# program4
animals = ["snake",'rabbit',"lion",'tiger']
animals.clear()
#print(animals)

# program5
numbers = [666,111,222,333,444,555,666,777,666]
q1 = numbers.count(666)
print(q1)

# program 6
#           0   1   2   3   4   5   6   7   8
numbers = [666,111,222,333,444,555,666,777,666]
numbers.append(888)
print(numbers)
numbers.insert(2,888)
print(numbers)

# program 7
numbers = [666,111,222,333,444,555,666,777,666]
numbers.reverse()
print(numbers)

# program8
#          0    1   2   3   4  5    6   7  8
numbers = [666,111,222,333,444,555,666,777,666]
q2 = numbers.index(111)
q3 = numbers.index(666,3)
#q4 = numbers.index(6666)
print(q2)
print(q3)



x = 10
y = x
y = 900
print(x) # 10
print(y) # 900

# program 2
names = ["amol","ram","sham"]
names2 = names 
names2[0] = "amit"

print(names)
print(names2)

cities = ["pune","mumbai","bangalore"]
citiesB  = cities 
cities[0] = "wardha"

print(cities)
print(citiesB)


# program 9

country = ["india","srilanka","pakistan"]
countriesB = country.copy()
countriesB[0] = "bharat"
print(countriesB)
print(country)

country.sort()
print(country)

marks = [11,22,33]
marksB = [44,55,66]

marksB.extend(marks)
print(marksB)
