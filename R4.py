# #LIST

# names=["subhuti","shruti","shivmala","shamli"]
# print(names)
# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])


# print(type(names))

# x=10
# print(x)
# print(type(x))

# y=2.4
# print(y)
# print(type(y))
# z="subhuti"
# print(z)
# print(type(z))

# a=True
# print(a)
# print(type(a))

# #program 2
#cities=["pune","mumbai","nagpur","banglore"]
# print(cities)
# print(type(cities))

# #for loop with range 
state=["MH","MP","UP","RJ"]
for i in range(len(state)):
    print(i)
    print(state[i])

# for without range
citiesT=["pune","mumbai","nagpur","banglore"]
for x in citiesT:
    print(x)


#while loop
q1=0
while(q1<len(state)):
    print(q1)
    q1=q1+1


x = 10
print(x)

# list 

names = ["subhuti",'shruti',"shivmala","msnsi","shanu"]
numbers = [11,22,33,44,55,66]
canDrive = [True, False , True , False]
info = ["subhuti","kapse",745894359]

print(names)
print(type(names))

x = 10 
print(type(x))

y = 10.5 
print(type(y))

c = "subhuti"
print(c)
print(type(c))


fruits = ["apple","mango","grapes","papaya"]
print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])


# program 2

cities = ['pune',"nagpur","bangalore","kolkata"]

print(cities[-1])
print(cities[-2])


# program 3
# for loop with range and for loop with range
            
country = ["india","pakistan","bangladesh","srilanka","china"]
print(len(country))

for x in range(5):
    print(country[x])


state = ["MH","MP","UP","RJ"]
for x in range(len(state)):
    print(state[x])


# for loop without range
for x in state:
    print(x)

# loop over list - while loop
         
animals = ["tiger","lion","rabbit","snake"]
for x in range(len(animals)):
    print(animals[x])

for animal in animals:
     print(animal)

i1 = 0
while(i1 < len(animals)):
    #print(i1)
    print(animals[i1])
    i1 = i1 + 1




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
         
numbers = [666,111,222,333,444,555,666,777,666]
q2 = numbers.index(111)
q3 = numbers.index(666,3)
#q4 = numbers.index(6666)
print(q2)
print(q3)



x = 10
y = x
y = 900
print(x)
print(y) 

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
marksB = [44,55,66,77,88,99,77]

marksB.extend(marks)
print(marksB)



q1=marksB.count(77)
print(q1)


numI=[11,22,33,44]
a1=numI.copy()
a1[0]=99
print(a1)


names = ["subhuti","shruti","kamlesh","vimlesh","jitesh"]
print(names)

print(type(names))

# loop
for x in range(len(names)):
    #print(x)
    print(names[x])

for item in names:
    print(item)

i1 = 0
while(i1 < len(names)):
    print(i1)
    i1 = i1 + 1

# methods 
#            0        1        2       3
# adding the element
fruits  = ["apple","mango","banana","chikoo"]
print(fruits)

fruits.append("papaya")
print(fruits)

fruits.insert(2,"grapes")
print(fruits)

# program 2
vegetables  = ["brinjal","potato","tomato","cabbage","cauliflower"]
# remove the last element
vegetables.pop()
print(vegetables)
# remove by index
vegetables.pop(2)
print(vegetables)
# remove by element name 
vegetables.remove("cabbage")
print(vegetables)

# program 3
numbers = [11,22,33,44,55,66]
numbers.clear()
print(numbers)

# program 4
cities = ["pune","mumbai","banglore","kolkata","chennai"]
cities.reverse()
print(cities)

cities.sort()
print(cities)

# program 5
marks = [11,22,33,44,55]
marksB = [55,66,77,88,99,100,66]
marks.extend(marksB)
print(marks)

e = marksB.count(66)
print(e)

numbersM = [11,22,33]
e = numbersM.copy()
e[0] = 111

# numberB = numbersM
# numbersM[1] = 111
# print(numberB)
# print(numbersM)

print(e)
print(numbersM)



 