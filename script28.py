# compile time  ---syntax error

def add():
     print(8+8)

#run time  
#program 2

x = int(input("Enter the value 1 "))
y = int(input("Enter the value 2 "))
print(x/y)

# listA = [11,22,33,44]
# print(listA[4]) 

#program3
def calculateBonusPlusSalary(salary):
    return 0.10 * salary
print(calculateBonusPlusSalary(1000))
print("hello")
try:
    x = int(input("Enter the value 1 "))
    y = int(input("Enter the value 2 "))
    print(x/y)
except Exception:
    print('Invalid input')
print("bye")

#program 4
try:
    names = ["subhuti","sapeksha","shyli"]
    x = int(input("Enter the value 1 "))
    y = int(input("Enter the value 2 "))
    print(x/y)
    print(names[2])
    print(a)

except ArithmeticError:
    print('Invalid input')
except IndexError:
    print("increase value of your list")
except NameError:
    print("not defined")
except Exception:
    print("something went wront")
print("bye")

#program 5

try:
    names = ["shruti","shamli","vibhisha"]
    x = int(input("Enter the value 1 "))
    y = int(input("Enter the value 2 "))
    print(x/y)

except ArithmeticError:
    print('Invalid input')

finally:
    print("I will always execute")

#program 6

try:
    x = int(input("Enter the value 1 "))
    y = int(input("Enter the value 2 "))
    print(x/y)

except ArithmeticError:
    print('Invalid input')

else:
    print("hello")

#program 7
print('hello')
try:
    x1 = int(input("Enter the value 1 "))
    y1 = int(input("Enter the value 2 "))
    print(x/y)

except ArithmeticError:
    print('Invalid input')
else:
    print("hello")
finally:
    print("i willl always... ")
print("bye")


# A single try block can be follwed by several except block 
# Multiple except blocks can be used to handle multiple excpetions 
# We cannot write except block with try block
# Else block and finally block are not compulsory
# Whem there is no exception else block is executed after try block 
# Finally block is always executed




#program 1
#compile time error
def add():
    print(2+4)

#run time error
print("hello")
q1=int(input("please enter the numberA"))
q2=int(input("Enter the numberB"))    
print(q1/q2)
print("bye")

print("hello")
numbers=[11,22,3,4,5,6]
print(numbers[5])
print("bye")

#logical error
def calculatorBonusSalary(amount):
    return amount * 0.10
print(calculatorBonusSalary(10000))

#program 2

print("hello")
try:
    e=int(input("enter the number A"))
    f=int(input("enter the number B"))
    print(e/f)
except Exception:
    print("please enter correct input")  
    print("bye")  


#try  except  else  finally
#program 3
print("hello")
names = ["subhuti","shruti","sanu","samy"]
try:
    e = int(input("enter the number A"))
    f = int(input("enter the number B"))
    print(e/f)
    print(names[9])

except ArithmeticError:
    print("please enter correct input")
except IndexError:
    print("add more element to list")
except Exception:
    print("Please correct the values")
print("bye")


#program 4

print("hello")
try:
    e = int(input("enter the number A"))
    f = int(input("enter the number B"))
    print(e/f)
except ArithmeticError:
    print("please enter correct input")
finally:
    print("I will always execute")
print("Bye")

#program 5

print("hello")
try:
    a1=int(input("enter the number A"))
    a2=int(input("enter the number B"))
    print(a1/a2)
except ArithmeticError:
    print("please enter correct input")
else:
    print("hello i will run")  
finally:
    print("I will always execute")
    print("bye")


