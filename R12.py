# program 1

birthYear = [1989,1990,1991,1992]
ages = []

for x in birthYear:
    #print(x)
    #print(2024 - x)
    age = 2024 - x
    ages.append(age)
print(ages)

age2 = list(map(lambda x : 2024 - x,birthYear))
print(age2)


# program 2
numbers = [11,22,33,44,55]
#[21,32,43,54,65]
plus10 = list(map(lambda x:x+10,numbers))
print(plus10)


#program 3
marks = [78,60,44,55,66,77,44,55,66]
above60 = []
for x in marks:
    #print(x)
    if x > 60:
        above60.append(x)
print(above60)

# filter
above602 = list(filter(lambda x : x > 60,marks))
print(above602)

# program 4
transactions = [89,22,-33,-44,5,6,-77,88,99]
deposit = list(filter(lambda x:x > 0,transactions))
print(deposit)

withdrawl = list(filter(lambda x:x < 0,transactions))
print(withdrawl)

# program 5
evenOdd = [18,16,14,23,17,25,16,18]
even = list(filter(lambda x : x % 2 == 0,evenOdd))
print(even)

odd = list(filter(lambda x : x % 2 != 0,evenOdd))
print(odd)

# program 6
numbers  = [11,22,33]
total =  0 

for x in numbers:
    total = total + x
print(total)

from functools import reduce
e = reduce(lambda acc,el:acc+el,numbers)
print(e)