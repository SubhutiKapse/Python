# list comprehension
lst = [1989,1990,1991,1992]
# [35,34,33,32]
ages  = []
for x in lst:
    ages.append(2024-x)
print(ages)

# program 2
# [expression-loop-condition]
a = [2024 - x for x in lst]
print(a)

# program 3
number = [1,2,3,4,5,6,7,8,9,10]
c = [x * x for x in  number]
print(c)



# program 4
d = [x for x in number if x % 2 == 0]
print(d)



# program 5
number = [1,2,3,4,5]
#["odd","even","odd","even","odd"]

e = ["even" if x % 2 == 0 else "odd" for x in number]
print(e)



# program 6
names = ["subhuti","sapeksha","shanu","shyli","shruti"]

f = ["Mr/Mrs"+ x for x in names if len(x) > 5]
print(f)