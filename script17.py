# lamda function 
def addA(x,y):
    return x + y
e = addA(22,3)
print(e)

add = lambda x,y:x+y
f = add(235,6)
print(f)



# program 2
e = lambda x:x*x
print(e(4))

# program 3
def addition(x,y):
    return x + y
print(addition(12,4))

# function as parameter to another function
add = lambda x , y : x + y
def addition(fn,x,y):
    # fn = lambda x , y : x + y
    f = fn(x,y)
    return f 
e2 = addition(add,13,4)
print(e2)

sub  = lambda x,y:x-y 
def subtraction(fn,s,t):
    #fn = lambda x,y:x-y 
    # s = 12
    # t = 6

    e = fn(s,t)
    return e
e2 = subtraction(sub,12,6)
print(e2)

# program 4
# function as a return type 
def add():
    return lambda x,y :x+y
e = add()
print(e)
e2 = e(12,3)
print(e2)