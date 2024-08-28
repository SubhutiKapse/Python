# LAMBDA FUNCTION
# lamdba - keyword
# x , y - parameter 
# x + y - return 
add = lambda x,y:x+y
print(add(12,3))

sqrt = lambda x : x * x
print(sqrt(12))

cube  = lambda x: x * x * x
print(cube(9))

# function as a parameter

sub = lambda x,y:x-y

def subtraction(fn,x,y):
    # x = 24 
    # y = 12
    # fn = lambda x,y:x-y
    e = fn(x,y)
    return e

q9 = subtraction(sub,24,12)
print(q9)


add = lambda x , y : x + y
def addition(fn,x ,y):
    # x - 12
    # y - 3 
    # fn = lambda x , y : x + y
    e = fn(x,y)
    return e
q10 = addition(add,12,3)
print(q10)




# function as a parameter to another function 
add = lambda x,y:x+y
def addition(fn,x,y):
    #fn = lambda x,y:x+y
    # x = 12
    # y = 3

    e = fn(x,y)
    return e

q1 = addition(add,12,3)
print(q1)

# program 2
# function as a return type
def subtraction():
    return lambda x,y:x-y
sub = subtraction()
print(sub)

#sub = lambda x,y:x-y
e = sub(12,4)
print(e)



# program 3
# default parameter
def multiplication(x=4,y=2):
    print(x*y)
multiplication(12,3)
multiplication()
multiplication(10)

#program 4
#positional argument 
def division(x,y):
    print(x/y)
division(y=8,x=16)

# program5
def addAll(*args):
    print(args) # (12,4,3,4)
    total = 0
    for x in args:
        total = total + x
    return total
q = addAll(12,4,3,4)
print(q)


# program -1
# default argument
def add(x = 2, y = 4):
    print(x+y)
add(10)  # 14
add() # 6
add(11,4) # 15

# program - 2
# positional arguments 
def add(x,y):
    print(x-y)
add(y = 33,x = 5)

# program - 3
# *args
def addition(*args):
    print(args)
    total = 0 
    for x in args:
        total = total + x
    return total
q2 = addition(1,2,3,4,5,6)
print(q2)

# program - 4
# **kwargs 
def addCity(**args):
    print(args)
    args['city'] = "banglore"
    return args
q3  = addCity(firstName ="subhuti",lastName="kapse",rollNo = 23)
print(q3)

# program 5
birthYear = [1989,1990,1991,1992]
ages = [] # [35]
#[35,34,33,32]
for x in birthYear:
    age = 2024 - x
    ages.append(age)
print(ages)

# program 6
marks = [44,55,66,77,22,33,45,66]
above50 = []
for x in marks:
    if x > 50:
        above50.append(x)
print(above50)

# program 7
numbers = [11,22,33]
total = 0 
for x in numbers:
    total = total + x 
print(total)

#program 8
cities = ["pune","wardha","kolkata"]
for x in cities:
    print("welcome "+x)


    # program 1
# function as a parameter to another function 
add = lambda x,y:x+y
def addition(fn,x,y):
    #fn = lambda x,y:x+y
    # x = 12
    # y = 3

    e = fn(x,y)
    return e

q1 = addition(add,12,3)
print(q1)

# program 2
# function as a return type
def subtraction():
    return lambda x,y:x-y
sub = subtraction()
print(sub)

#sub = lambda x,y:x-y
e = sub(12,4)
print(e)

# program 3
# default parameter
def multiplication(x=4,y=2):
    print(x*y)
multiplication(12,3)
multiplication()
multiplication(10)

#program 4
#positional argument 
def division(x,y):
    print(x/y)
division(y=8,x=16)

# program5
def addAll(*args):
    print(args) # (12,4,3,4)
    total = 0
    for x in args:
        total = total + x
    return total
q = addAll(12,4,3,4)
print(q)




###########


# program -1
# default argument
def add(x = 2, y = 4):
    print(x+y)
add(10)  # 14
add() # 6
add(11,4) # 15

# program - 2
# positional arguments 
def add(x,y):
    print(x-y)
add(y = 33,x = 5)

# program - 3
# *args
def addition(*args):
    print(args)
    total = 0 
    for x in args:
        total = total + x
    return total
q2 = addition(1,2,3,4,5,6)
print(q2)

# program - 4
# **kwargs 
def addCity(**kwargs):
    print(kwargs)
    kwargs['city'] = "pune"
    return kwargs
q3  = addCity(firstName ="chinmay",lastName="Deshpande",rollNo = 23)
print(q3)

# program 5
birthYear = [1989,1990,1991,1992]
ages = [] # [35]
#[35,34,33,32]
for x in birthYear:
    age = 2024 - x
    ages.append(age)
print(ages)

# program 6
marks = [44,55,66,77,22,33,45,66]
above50 = []
for x in marks:
    if x > 50:
        above50.append(x)
print(above50)

# program 7
numbers = [11,22,33]
total = 0 
for x in numbers:
    total = total + x # 66
print(total)

#program 8
cities = ["pune","wardha","kolkata"]
for x in cities:
    print("welcome "+x)