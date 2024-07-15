# # print("hello")

# # x=10
# # print(x)
# # y=34
# # print(y)

# # #arithmetic operation
# # # + -/ * %
# # d=10
# # e=5
# # print(d+e)
# # print(d-e)
# # print(d/e)
# # print(d%e)
# # print(d*e)


# # def Cal(x,y):
# #     print(d+e)
# #     print(d-e)
# #     print(d/e)
# #     print(d%e)
# #     print(d*e)
# # Cal(12,4)    


# # x=20
# # print(x)

# # s=True
# # print(s)

# # #function without parameters and without returntype
# # def add():
# #     print(2+1)
# # add()
# # add()
    
# # #function with parameters and without returntype
# # def addA(x,y):
# #     print(x+y)
# # addA(2,4)    
# # #function with parameters and with returntype
# # def addB(x,y):
# #     return x+y
# # a1=addB(2,4)
# # print(a1)


# # #function without parameters and without returntype
# # def sub():
# #     print(4-3)
# # sub()    
# # #function with parameters and without returntype
# # def subA(a,b):
# #     print(a-b)
# # subA(4,7)    
# # #function with parameters and with returntype
# # def subB(e,f):
# #     return e-f
# # q1=subB(4,6)
# # print(q1)



# #conditional statement
# #if condition
# num=20
# if num <=302 and num>60:
#  print("10 % discount")
# if num>3 and num>6:
#  print("20 % discount")
# if num <=300 and num>67:
#  print("30 % discount")


#  if num <=302 and num>60:
#   print("10 % discount")
# elif num>3 and num>6:
#   print("20 % discount")
# elif num <=300 and num>67:
#   print("30 % discount")


# #list
# names=["subhuti","anamika","vrushali","sayli","anehal"]
# print(names)


x=23
print(x)

y=True
print(y)

a=2
b=4
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)

#arithmetic operator




#program 1

h1=[22,33,44,55]
print(h1)
print(type(h1))
print(h1[0])


#program 2
names=["subhuti","shruti","kalpana","shivmala"]
print(names)
print(type(names))
print(names[0])
print(names[1])
print(names[2])
print(names[3])


for x in range(len(names)):
   print(x)


for x in names:
   print(x)

fruits=["apple","banana","orange","grapes"]
print(fruits)
print(len(fruits))
q2=len(fruits)   
print(q2)

for x in range(len(fruits)):
   print(x)


for x in fruits:
   print(x)

fruits.append("straberry")
print(fruits)   


num=[11,22,33,44,55,11]
a1=num.count(11)
print(a1)