lst=[1989,1990,1991,1992]
#[35,34,33,32]
ages=[]
for x in lst:
    ages.append(2024-x)
    print(ages)

#program 2
    #[expression-loop-condition]
q1= [2024-x for x in lst]    
print(q1)

#program 3
num=[1,2,3,4,5,6,7,8,9,10]
q2=[x*x for x in num]
print(q2)
#program 4
q3=[x for x in num if x %2 ==0]
print(q3)
#program 5
number=[1,2,3,4,5]
#["odd","even","odd","even","odd"]

e=["even" if x %2==0 else "odd" for x in number]
print(e)
#program 6

names=["subhuti","sapeksha","shimli","shyli"]
r1=["Mr/Mrs" + x for x in names if len(x)>5]
print(r1)

#list comprehension
lst=[1985,1986,1987,1988,1999]
agesA=[]
for x in lst:
    ages.append(2024-x)
    print(ages)

r1=[2024 - x for x in lst]
print(r1)

number=[5,6,7,8,9,10]
num=[]
for x in number:
    num.append(20-x)
    print(x)

r2=[20- x for x in number]
print(r2)

numbersA=[1,2,3,4,5,6,7,8,9,10]
r3=[x*x for x in numbersA]
print(r3)

numbersB=[1,2,3,4,5,6,7,8,9,10]
r4=[x for x in numbersB if x%2==0]
print(r4)

r5=["even" if x %2==0 else "odd" for x in numbersB]
print(r5)

