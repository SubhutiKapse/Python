#program 1
str='cat man sun mpo run mat m9 sun'
# str ='The morning meeting will be scheduled at 8am or 9am,evening at 8pm or 9pm'
# q1= re.findall(r'\d[a-z]\d[a-z]*',str)
# print(q1)
e=re.search(r'm\w\w',str)
f=re.search(r'\wun',str)