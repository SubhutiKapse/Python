#program 1
try:
    names = ["subhuti","sanu","shibra"]
    a = int(input('Enter a numberA'))
    b = int(input('Enter the number B'))
    print(a/b)
    print(names[4])
except ArithmeticError:
    print("please enter correct input")
except IndexError:
    print('please add more values to list')




#program2 
print("hello")
try:
    print(34/0)
finally:
    print("i will always execute")
print("bye")





#program 3
def calAvg(list):
    [11,22,33][4]
    total = 0
    for item in list:
        total = total + item 
    avg = total/len(list)
    return total,avg
try:
    a,b = calAvg([1,2,3,'a'])
    print(a)
    print(b)
except TypeError:
    print('enter the correct input')
except ZeroDivisionError:
    print('Arithmetic exception , enter correct value')
except Exception:
    print("please enter correct input")

print("hello")
try:
    x = 18
    assert x > 1 and x <= 9
    print(x)
except AssertionError:
    print("condition not matched")
print("bye")