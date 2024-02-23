# #program 1
# setA={11,22,33,44,33}
# print(setA)

# #program 2
# # setB={111,222,333,44,33}
# # print(setB[0])#does not stores the value by Index

# #program 3
# setC={"subhuti","shruti","shivmala","sujata"}
# print(setC)
# print("subhuti" in setC)
# print(len(setC))
# print(type(setC))

# city=["nagpur","pune","hyderabad","banglore"]
# print(city)
# print(len(city))
# print(type(city))

# for x in range(len(city)):
#     print(x)


# for x in city:
#  print(x)

# # for y in range(4):
# #    print(city[x])
 
#  #methods
#  #1..add()
#  setC={11,22,33,44}
#  setC.add(559)
#  print(setC)

#  #2..clear()
#  setD=["subhuti","shruti","shivmala"]
#  setD.clear()
#  print(setD)

# #3..pop(), remove(element)
# setE=["ram","sham","pushpindar","jay","veeru"]
# setE.remove("jay")
# print(setE)
# setE.pop()
# print(setE) 

# #4..update()
# setF={"subhuti","shruti","shivmala","lavi"}
# setF.update(["kamla","vimla"])
# print(setF)

# #setG={"ram","sham","babubhaiya","jogindar"}
# #setE = setG.copy()
# # setG.remove("ram")
# print(setE)
# # print(setA)


# #5..union()
# setH={11,22,33,44,55}
# setI={66,77,88,99,10}
# setJ=setH.union(setI)
# print(setJ)

# #6..intersection()
# setK={11,22,33,44,55}
# setL={11,77,33,99,10}
# setM=setK.intersection(setL)
# print(setM)

#7..intersection_update()
# setN={111,222,335,447,55}
# setO={115,757,373,99,10}
# setN.intersection_update(setO)
# print(setN)

#8..symmetric_difference()
setN={21,22,23,24}
setM={25,26,27,28}
setO=setN.symmetric_difference(setM)
print(setO)


#9..symmetric_difference_update()
setP={21,22,23,24}
setQ={21,26,27,28}
setR=setP.symmetric_difference_update(setQ)
print(setR)


#10..difference_update()

setP={21,2,3,24}
setQ={21,26,27,28}
setQ.difference_update(setP)
print(setQ)

#11..issuperset()
setR={11,22,33}
setS={11,22,33,44}
e=setR.issuperset(setS)
f=setS.issubset(setR)
print(e)

# #12..isdisjoint()

setR={11,22,33}
setS={11,44,55,66}
h=setR.isdisjoint(setS)
print(h)

#13..discard()
setT={11,22,33,44}
p=setT.discard(44)
print(p)