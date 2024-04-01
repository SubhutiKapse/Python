setA = {1,2,3}
setB = {11,22,33}
setC = setA.union(setB)
print(setC)


setE = {11,33,44}
setF = {44,55,66}
# setG  = setE.intersection(setF)
# print(setG)

#setE.intersection_update(setF)
setF.intersection_update(setE)
print(setE)
print(setF)

# program 2

setQ = {11,22,33}
setE = {45,66,77,33}

setR = setQ.symmetric_difference(setE)
print(setR)
setQ.symmetric_difference_update(setE)
print(setQ)
print(setE)


setQ = {11,22,33}
setE = {45,66,77,33}

setW = setQ.difference(setE)
print(setW)
setQ.difference_update(setE)
print(setQ)

setE.difference_update(setQ)
print(setE)


#program 4
setQ = {11,22,33}
setE = {11,22,33,44}
q = setQ.issubset(setE)
q2 = setE.issuperset(setQ)
print(q)
print(q2)

setQ = {11,22,33,44,88}
setF = {55,66,77,88}
e = setQ.isdisjoint(setF)
print(e)

# program 5

setW = {11,22,33,44}
setW.add(55)
print(setW)

setW.clear()
print(setW)

#setW.pop()
#setW1 = {11,22,33,44}
#setW.remove(44)

setW.update({5,6,7,8,3})
print(setW)

r = setW.discard(56)
print(setW)