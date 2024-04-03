#compile - time error---syntax error

def addition(x,y):
 print(x+y)#indentation error
addition(12,3)



#run time error 
print("hello")
x = int(input('enter the number one'))
y = int(input('enter the number two '))
print(x/y)
print("bye")



#logical error
def add10Pr(amount):
    return amount * 0.10 
e = add10Pr(100)
print(e)


# program 3
print("hello")
try:
    x = int(input('Enter the number A'))
    y = int(input('Enter the number B'))
    print(x/y)
except Exception:
    print("invalid input")
print('bye')