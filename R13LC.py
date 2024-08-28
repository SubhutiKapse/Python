# list comprehension 
# return type will always be []
#[expression:loop:condition(only one condition)]


birthYear = [1989,1990,1991,1992] 
ages = [] # [35,34,33,32]

for x in birthYear:
    age = 2024 - x
    ages.append(age)
print(ages)

e1 = list(map(lambda x : 2024-x,birthYear))
print(e1)

#[expression:loop:condition]
e2 = [2024 - x for x in birthYear]
print(e2)

# program 2
numbers = [11,22,33,44,55]
e2 = [x + 10 for x in numbers]
print(e2)

#program 3 
marks = [44,55,66,77,88,55,44,88]
above60 = []

for x in marks:
    if x > 60:
        above60.append(x)
print(above60)
e3 = list(filter(lambda x :x >60,marks))
print(e3)

#[expression:loop:condition]
e3 = [x for x in marks if x > 60]
print(e3)

# program 3

numberB = [22,33,44,55]
# ["even","odd","even","odd"]

status = []
for  x in numberB:
    if x % 2 == 0:
        status.append("even")
    else:
         status.append("odd")
print(status)


#[tenary:loop]

# e2 = ["even" for x in numberB if x%2 == 0 ]
# print(e2)

# user ternary if more than one reference 
e4 = ["even" if x % 2 == 0 else "old" for x in numberB]
print(e4)


birthYear = [1989,1990,1992,1992]
ages = []

for x in birthYear:
   age =  2024 - x
   ages.append(age)
print(ages)

e = list(map(lambda x: 2024 - x,birthYear))
print(e)

#[expression : loop : condition(one condition)]
#[ternary[multiple contion]:loop]
print([2024 - x for x in birthYear])

# program 2
marks = [33,44,55,66,22,33,56]
above50 = []
for x in marks:
   if x >  50:
      above50.append(x)
print(above50)
      
above502 = list(filter(lambda x : x > 50,marks))
print(above502)
above503 = [x for x in marks if x > 50]

# program 3
numbers = [11,22,33,44,66,33]
evenOdd = []
for x in numbers:
   if x % 2 == 0:
      evenOdd.append("even")
   else:
      evenOdd.append("odd")
print(evenOdd)
print(list(map(lambda x:"even" if x % 2==0 else "odd",numbers)))
print(["even" if x % 2 == 0 else "odd" for x in numbers])

# program 4
numbersB  = [11,22,33]
total = 0
for x in numbersB:
   total = total + x
print(total)

from functools import reduce
print(reduce(lambda acc,el:acc+el,numbersB))



      
e2 = [2024 - x for x in birthYear]
print(e2)

# program 2
transactions = [9900,-1923,8000,4455,6666,-777,888,-444]

deposit = []
withdrawl =[]
for x in transactions:
    if x > 0:
        deposit.append(x)

print(deposit)

for x in transactions:
    if x < 0:
        withdrawl.append(x)

print(withdrawl)

deposit = list(filter(lambda x : x > 0 ,transactions))
withdrawl = list(filter(lambda x : x < 0 ,transactions))

deposit = [x for x in transactions if x > 0]
print(deposit)

withdrawl = [x for x in transactions if x < 0]
print(withdrawl)


# program 4 
numbers = [11,22,33]
total = 0 

for x in numbers:
    total = total + x 
print(total)

from functools import reduce
print(reduce(lambda acc, el:acc+el,numbers))

numbersB = [11,22,33,44]
#["odd","even","odd","even"]

evenOdd = []

for x in numbersB:
    if x % 2 == 0:
        evenOdd.append('even')
    else:
        evenOdd.append('odd')
print(evenOdd)

e2 = ["even" if x % 2 == 0 else "odd" for x in numbersB]
print(e2)


print([x * 2 for x in range(1,11)])