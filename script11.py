x = 10
print(x)

first_name = "subhuti"
print(type(first_name))


last_name = 'kapse'
print(type(last_name))


middle_name = """
raj

"""

info = '''
I am learning
javascript
'''
print(info)

# program 2
city = "pune"
# 0  1  2   3
# p  u  n   e
print(city[0])
print(city[1])
#print(city[5])

# program 3
city4 = "chandrapur"
# 0   1   2  3  4  5  6  7  8   9
# c   h   a  n  d  r  a  p  u   r
#-10 -9  -8 -7  -6 -5 -4-3 -2  -1
#strint[startIndex,EndIndex(not included),stepSize]
# e  = city4[5::]
# e2 = city4[-7::]
# e3 = city4[1:7:]
# e4 = city4[1:-2:]
# e5 = city4[-7:-2:]
# e6 = city4[-7:9:]
# e6 = city4[0:10:3]
# e7 = city4[::-1]
e8 = city4[-1:-4]
print(e8)

# program 4
city = "nagpur"
e9 = city.upper()
print(e9)

city2 = "Pune"
e10 = city2.lower()
print(e10)

city3 = "chandrapur"
e11 = city3.count('a')
print(e11)