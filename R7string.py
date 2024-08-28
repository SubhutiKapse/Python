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


# string methods 
firstName = "subhuti"
print(type(firstName))

e1 = firstName.upper()
print(e1)

lastName = "kapse"
e2 = lastName.lower()
print(e2)

middleName = "kamlesh"
e3 = middleName.capitalize()
print(e3)

# upper() , lower() , capitalize()

# program 2

firstName = "subhuti"
e4 = firstName.startswith("s")
e5 = firstName.startswith('su')
print(e4)
print(e5)

e6 = firstName.endswith('i')
e7 = firstName.endswith('ti')
print(e6)
print(e7)

# program 3
firstName = " subhuti "
print(len(firstName))

# e5 = firstName.strip()
# print(len(e5))

# e6 = firstName.lstrip()
# print(len(e6))

# e7 = firstName.rstrip()
# print(len(e7))

# program 4
str = "123213123123"
e8 = str.isdigit()
print(e8)

#isnum()

str2 = "amol"
e9 = str2.isalpha()
print(e9)

str3 = "mayur123"
print(str3.isalnum())


str3 = "123"
print(str3.isalnum())

str3 = "aaaa"
print(str3.isalnum())

str3 = "aaaa #"
print(str3.isalnum())


#program 5
str = "i am learning python"
e10 = str.replace("python","js")
print(e10)


str2  = "Hello"
e2 = str2.islower()
print(e2)


str3 = "HELLO"
e4 = str3.isupper()
print(e4)


str4 = "chinmaya"
e3 = str4.count('a')
print(e3)

str5 = "I Learn Python"
e4 = str5.istitle()
print(e4)

str6 = "I Am Learning  Python"
e5 = str6.swapcase()
print(e5)

#rjust()
#ljust()

# isspace()
str7 = " "
e8 = str7.isspace()
print(e8)

# varaibles -----> types ---- comparison ---- logical 
# conditional statements ----> loops ----- list 
# dictionary   strings  ----- tuple ----- set


#7:30pm

a = 10
print(a)
a = "hello"
print(a)

#int a = 124


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


city = "pune"
print(city[0])

# 0     1    2    3
# p     u    n    e
#-4    -3   -2    -1

# for loop 
for char in city:
    print(char)
# for loop with range 
for x in range(len(city)):
    #print(x)
    print(city[x])
# while loop
i1 = 0
while(i1 < len(city)):
    #print(i1)
    print(city[i1])
    i1 = i1 + 1

# program 3
#           0          1        2        3
names = ["chinmay",'shirish',"sarika","poorva"]
print(names[0])
names[1] = "sheerish"
print(names)

city2 = "nagpur"
#city2[1] = "y"
city2 = 'wardha'

# program 4
str = "mumbai"
e = len(str)
print(e)

# program 5
city3 = "wardha"
e2 = city3.upper()
print(e2)

city4 = "Kanpur"
e3 = city4.lower()
print(e3)

city5 = "chandrapur"
e4 = city5.startswith('cha')
e5 = city5.startswith('c')
e6 = city5.startswith('C')

print(e4)
print(e5)
print(e6)


city6 = "jaipur"
e7 = city6.endswith('r')
e8 = city6.endswith('pur')
e9 = city6.endswith('R')
print(e7)
print(e8)
print(e9)




#STRING METHODS




firstName = "subhuti"
print(type(firstName))

e1 = firstName.upper()
print(e1)

lastName = "kapse"
e2 = lastName.lower()
print(e2)

middleName = "Ajay"
e3 = middleName.capitalize()
print(e3)

# upper() , lower() , capitalize()

# program 2

firstName = "kamlesh"
e4 = firstName.startswith("r")
e5 = firstName.startswith('ra')
print(e4)
print(e5)

e6 = firstName.endswith('l')
e7 = firstName.endswith('Ul')
print(e6)
print(e7)

# program 3
firstName = " sanvi "
print(len(firstName))

# e5 = firstName.strip()
# print(len(e5))

# e6 = firstName.lstrip()
# print(len(e6))

# e7 = firstName.rstrip()
# print(len(e7))

# program 4
str = "123213123123"
e8 = str.isdigit()
print(e8)

#isnum()

str2 = "sapeksha"
e9 = str2.isalpha()
print(e9)

str3 = "sanu3948"
print(str3.isalnum())


str3 = "123"
print(str3.isalnum())

str3 = "aaaa"
print(str3.isalnum())

str3 = "aaaa #"
print(str3.isalnum())


#program 5
str = "i am learning python"
e10 = str.replace("python","js")
print(e10)


str2  = "Hello"
e2 = str2.islower()
print(e2)


str3 = "HELLO"
e4 = str3.isupper()
print(e4)


str4 = "chinmaya"
e3 = str4.count('a')
print(e3)

str5 = "I Learn Python"
e4 = str5.istitle()
print(e4)

str6 = "I Am Learning  Python"
e5 = str6.swapcase()
print(e5)

#rjust()
#ljust()

# isspace()
str7 = " "
e8 = str7.isspace()
print(e8)
























