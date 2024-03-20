#program 1
lst=[1989,1990,1991,1992]
ages=[]

for i in lst:
    x=2024-i
    ages.append(x)
    print(ages)

a=list(map(lambda x:2024-x,lst)) 
print(a)
print([2024-i for i in lst])

#program  2
q1=lambda x :2024-x
q1(lst[0])

#program 3
names=["subhuti","shruti","sapesksha","shyli"]
above5=[]
for x in names:
    above5.append(x)
    print(above5)

    print([x for x in names if len(x)> 5])
    w2=list(filter(lambda x :len(x)> 5,names))

transactions=[]
s1=[2,3,4,-12,-34,67,788]
for x in s1:
    if x<0:
        #print("withdrawl")
        transactions.append("withdrawl")
    else:
        transactions.append("deposit")
        print(transactions)
        print(["withdrawl" if x <0 else "deposit" for x in s1])
        #print(list(filter(lambda x: x>0,s1)))
        #print(list(filter(lambda x:x <0,s1)))

#program 1
        list=[1989,1990,1991,1991]
        age=[]
        for i in list:
            x=2024-i
            ages.append(x)
            print(ages)


#a=list(map(lambda x:2024-x,list)) 
#print(a)    
#print([2024-i for i in list])       

#program 2
p1=lambda x :2024 -x
p1(list[0])

#list comprehension

lst=[1989,1990,1991,1992]
agesA=[]
for x in list:
    agesA.append(2024-x)
    print(agesA)

 #progrm 2
    a1=[2024-x for x in lst]  
    print(a1) 

#program 3
        