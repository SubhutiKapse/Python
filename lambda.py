#program 1
def addA(x,y):
    return x+y
q1=addA(2,5)
print(q1)

#using lambda
add=lambda x,y:x+y
w1=add(20,5)
print(w1)
#program 2
def subA(a,b):
    return a-b
q2=subA(5,2)
print(q2)
#using lambda
sub=lambda a,b:a-b
w2=sub(20,10)
print(w2)

#program 3
def addition(x,y):
    return x+y
print(addition(7,7))

#function as parameter to another function
add=lambda x,y:x+y
def addition(fn,x,y):
    fn=lambda x,y:x+y
    f=fn(x,y)
    return f
q1=addition(add,12,4)
print(q1)


sub=lambda x,y:x-y
def subtraction(fn,s,y):
    fn=lambda x,y:x-y
    s=5
    y=6
    a=fn(s,y)
    return a
a1=subtraction(sub,6,3)
print(a1)

#program 4
#function as returntype
def add():
    return lambda x,y:x+y
r=add()
print(r)
r1=r(23,6)
print(r1)
