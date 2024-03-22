# x=10
# print(x)

# #arithmetic operation
# a=5
# b=3
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)


# #function without parameters and without returntype
# def add():
#     print(9+9)

# add()
# add()    
# #function with parameters and without returntype
# def sub(x,y):
#     print(x-y)

# sub(2,8)
# sub(9,7)    

# #function with parameters and with returntype
# def addA(u,v):
#     return u+v
# s1=addA(7,7)
# print(s1)

# #loops
# #for loops using range
# #print 1 to 10
# for x in range(11):
#     print(x)
# #print 10 to 1
#     for x1 in range(10):
#         print(x1)
# #print table of 2
#     for x in range(2,21,2):
#         print(x)
# #print table of 10
#     for x in range(10,101,10):
#         print(x)

#  #print table of 3
#         for x in range(3,31,3):
#             print(x)      

# #print reverse table of 3
#         for x in range(30,0,-3):
#             print(x)

# #print reverse table of 10
#             for x in range(100,9,-10):
#                 print(x)


# #break statement with for loops
# for x in range(1,6):
#     print(x)#1#2#
#     if x==3:
#      break

# for x in range(1,9):
#    if x==5:
#     break
# print(x)     

# for x in range(1,8):
#   print(x)
#   if x==4:
#     break
  
# for x in range(1,6):
#   if x==4:
#     break
#   print(x)  

# #continue with loops
#   for x in range(1,5):
#     if x==3:
      
#       continue
# print(x)


# #break
# for x in range(1,5):
#   if x==3:
#     break
#   print(x)

#   for x in range(1,10):
#     print(x)
#     if x==5:
#       break

# #continue
#     for x in range(1,8):
      
#       if x==6:
#         continue
#       print(x)


#       for x in range(1,7) :
        
#         if x==4:
#           continue   
#         print(x)


#  #while loops
# q1=1
# while(q1<=4):
#   print(q1)
#   q1=q1+1         

# #table of 2
#   q2=2
#   while(q2<=20):
#     print(q2)
#     q2=q2+2


# #table of 5
# q3=5
# while(q3<=50):
#   print(q3)
#   q3=q3+5        


# #table of 5 in reverse
#   w1=50
# while(w1>=5):
#  
#   #w1=w1+5 

# #   s1=2
# #   while s1<=20:
    
# #     if s1==5:
# #       break
# #     print(s1)
# #     s1=s1+2
  
#list
names=["subhuti","sapeksha","shivani","shyli"]
print(names)
print(type(names))
print(len(names))

names[0]
print(names)
names[1]
print(names)
names[2]
print(names)
names[3]
print(names)

names[0]="kamla"
print(names)
names[1]="shamli"
print(names)
for x in range(len(names)):
 print(x)

for  item in names:
 print(item) 

q1=0
while(q1<len(names)):
 print(q1)
 print(names[q1])
 q1=q1+1 

flowers=["rose","mogra","jasmine","tulip","lily"]
print(flowers)
print(type(flowers))
print(len(flowers))
print("lily" in flowers)

a1=1
while(a1<=5):
 if a1==3:
  a1=a1+1
  print(a1)

  