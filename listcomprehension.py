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