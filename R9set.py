# #SETS
# #sets is defined in curly braces
# #does not stores values by index
# setA={11,22,33,44,55,66}
# print(setA)
# #print(setA[0])#does not stores value by index

# # element available in set
# #using in operator
# print(44 in setA)


# #for loop
# setB={"subhuti","shruti","sanu","sanvi"}
# for item in setB:
#     print(item)

# setC={11,22,33,44}
# print(len(setC))



# #SET METHODS

# # add()
# # pop()
# # remove()
# # copy()
# # clear()
# # update()
# #union()
# #intersection()
# # intersection_update()
# # difference()
# # difference_update()
# # symmetric_difference()
# # symmetric_difference_update()
# # issuperset()
# # issubset()
# # isdisjoint()



# # #add()
# # setA={11,22,33}
# # print(setA)
# # setA.add(44)
# # print(setA)


# # #pop()-last element remove
# # setB = {11,22,33}
# # setB.pop()
# # print(setB)


# # #remove()-remove any element
# # setC = {11,22,33,44,55}
# # setC.remove(44)
# # print(setC)

# # copy()
# setD={11,22,33,44}
# setE={55,66,77}
# setD=setE
# setF=setD.copy()
# print(setF)
# # clear()
# setG={11,22,33,44,55}
# setG.clear()
# print(setG)
# # update()
# setH={66,77,88,99}
# setH.update([57,67])
# print(setH)
# #union()
# setI={11,22,33}
# setJ={44,55,66}
# setK=setI.union(setJ)
# print(setK)
# #intersection()
# setL={11,22,33,44,55}
# setM={11,33,55}
# setN=setL.intersection(setM)
# print(setN)
# # intersection_update()
# setO={11,22,33}
# setP={11,22,7}
# setQ=setO.intersection_update(setP)
# print(setQ)
# # difference()
# setA = {11,22,33}
# setB = {44,55,66,33}
# print(setA.difference(setB))
# print(setB.difference(setA))
# # difference_update()
# setA = {11,22,33}
# setB = {44,55,66,33}
# setC=setA.difference_update(setB)
# print(setC)
# # symmetric_difference()
# setD = {11,22,33}
# setE= {44,55,66,33}
# print(setD.symmetric_difference(setE))
# # symmetric_difference_update()
# setD = {11,22,33}
# setE= {44,55,66,33}
# setD.symmetric_difference_update(setE)
# print(setD)
# # issuperset()-return boolean value
# setE = {11,22,33}
# setF= {11,22}

# print(setE.issuperset(setF))


# # issubset()-return boolean value
# print(setF.issubset(setE))
# # isdisjoint()-return boolean value
# setG = {11,33}
# setH = {44,22,11}
# print(setG.isdisjoint(setH))



# setA = {11,22,33,44,55,66,66}
# print(setA)
# # set stores the value by index ??
# #print(setA[0]) No
# # how to define set ?

# setB = {"subhuti","shruti","shamli","shyli","sakhi"}
# print(setB)

# # how to find value available in set ?
# setB = {"subhuti","shruti","shamli","shyli","sakhi"}
# print("subhuti" in setB)#true
# print("Subhuti" in setB)#false--S is capital
# # how loop over set ?

# setE = {"pune","mumbai","banglore","kolkata","chennai"}
# for x in setE:
#     print(x)


# #  dict - No , tuple - Yes , List - Yes , String - Yes
# #  set - No 

# # does set allows you to store duplicate values?

# listA = ["subhuti","subhuti","subhuti"]
# print(listA)

# tupleA = ("subhuti","subhuti","subhuti")
# print(tupleA)

# setA = {"subhuti","subhuti","subhuti"}

# dictA  = {
#     "age":12,
#     "age2":13
# }
# print(dictA)


# # how to find the length of set
# setD = {11,22,33,44,55}
# print(len(setD))

# # methods 
# # add()
# setA = {11,22,33,44,55}
# setA.add(66)
# print(setA)

# # clear()
# setA.clear()
# print(setA)


# setF = {11,22,33,44,55}
# # setG = setF
# # setG.add(4444)
# # print(setG)
# # print(setF)
# setE = setF.copy()
# setE.add(555555)
# print(setE)
# print(setF)


setQ={11,22,33}
setR={44,55,66}
setW=setQ.union(setR)

# program 2
setC = {11,22,33,22}
setD = {44,55,66,11,33}
e = setC.intersection(setD)
print(e)
setC.intersection_update(setD)
print(setC)

# program 3

setG = {44,55,66}
setH = {66,77,88}

print(setG.difference(setH))
print(setH.difference(setG))

# setG.difference_update(setH)
# print(setG)

setH.difference_update(setG)
print(setH)

# program 4

setK = {11,22,33,44}
setH = {44,55,33}

print(setK.symmetric_difference(setH))
setK.symmetric_difference_update(setH)
print(setK)

# program 5
setH1 = {66,77}
setH2  = {88,55,33}
#print(setH1.isdisjoint(setH2))

setH1.update([122,33,44])
print(setH1)

# program 6

setN = {11,22}
setM = {11,22,33,66}

print(setN.issubset(setM))
print(setM.issuperset(setN))