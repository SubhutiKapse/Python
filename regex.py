import re
#program 1
#\w-A-Z a-z 0-9
#\W -non alphanumeric
# str='cat man sun mpo run mat m9 sun'
# e=re.search(r'm\w\w',str)
# f=re.search(r'\wun',str)
# print(e)
# print(f)

#none--->python ---false value
# if e:
#     print(e.group())
# else:
#     print("match not found !")
# if f:
#         print(f.group())
# else:
#   print("match not found")        

#program 2 #findall
strB="man sun mop run mat fat cat sat"
q=re.search(r'\w\wp',strB)
if q:
    print(q.group())
else:
    print("not found")
q2=re.findall(r'm\w\w',strB)    
q3=re.findall(r'\wat',strB)    
print(q2)
print(q3)


#program 3
#match
strD="This is the 'core python's book"
q5=re.split(r"\w+",strD)
print(q5)
info='subhuti:911945700'
print(re.split(r'\w+',info))

#program 4
#sub
strW="I am learning javascriptt"
a1=re.sub(r'javascript','python',strW)
print(a1)


#search().findall(),match(),split(),sub()
#program 5
