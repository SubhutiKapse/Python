#program 1
#x,y ---formal arguments
#12,23--- actual arguments

def addA(x,y):
    return x +y
q1=addA(12,23)
print(q1)


#program 2 positional arguments
def subA(x,y):
    return x-y
w1=subA(x=23, y=12)
print(w1)

#program 3 default arguments
def mulA(x=10,y=5):
    return x*y
a1=mulA()
a2=mulA(3,5)
print(a1)
print(a2)

#program 4 variable length arguments
def addAll(*args):
    print(args)
    total=0
    for i in args:
       total =total +i    
    return total

w3=addAll(1,2,3,4,5,6,7,8,9,)
print(w3)

#program 5
def greet(*args):
    for i in args:
     print("welcome "+i)
    greet("pune","nagpur","mumbai")



#program 6
#a=12
#b=2.4
#c=true
#d=[11,22,33] 
#e=12,34
#r={
  #  "fristNAme":"subhuti"
  #  }           
 #s={1,2,3,4}
    #t="subhuti" 


def printInfo(**kwargs):
   print(kwargs)  
   for i in kwargs:
      print(i,kwargs[i])
printInfo(first_name="subhuti",last_Name="kapse",age=21,city="nagpur")          