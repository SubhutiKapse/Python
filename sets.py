#program 1
setA={11,22,33,44,33}
print(setA)

#unique values
#sets does not store the value by index


#program 2
setB={"subhuti","shruti","shivmala",22}
print(setB)
print("subhuti" in setB)
print(len(setB))

setC={"nagpur","chandrapur","pune","mumbai"}
print(setC)
print(type(setC))
print(len(setC))


city=["nagpur","chandrapur","pune","mumbai"]
for item in city:
    print(city)


print(len(city))


#sets methods
#add
setD={"subhuti","kamla","vimla","jamla"}
setD.add("shyli")
print(setD)

setE={11,22,33,44}
setE.add(345)
print(setE)
q1=setE.add(345969)
print(q1)

#clear
setE={"nagpur","chandrapur","pune","mumbai"}
setE.clear()
print(setE)

#pop(),remove(element)
setF={"subhuti","kamla","vimla","jamla","shyli"}
setF.remove("shyli")
print(setF)
setF.pop()
print(setF)


#update()

setG={"nagpur","chandrapur","pune","mumbai"}
setG.update(["rampur","kanpur"])
print(setG)


setH={"ram","jhilpesh","kamlesh","vimal"}
setI=setH
setI.remove("ram")
print(setI)
print(setH)


setJ={"ram","jhilpesh","kamlesh","vimal"}
setK=setJ.copy()
setK.remove("ram")
print(setJ)
print(setK)

#union()
setL={11,22,33}
setM={44,55,66}
setA=setL.union(setM)
print(setA)
#intersection()
setO={34,56,67,89}
setP={34,56,78}
setR=setO.intersection(setP)
print(setR)

# #program 1
# names=["subhuti","shruti","shivaay","kamlesh"]
# print(names)

# #program 2 dictionary
# info={
#     "firstName":"subhuti",
#     "lastName":"kapse",
#     "rollno":"11163",
#     "age":21
# }

setA={11,22,33,44}
print(type(setA))

#dont allow duplicate values
setB={11,22,33,44,55,55,66,66}
print(setB)
print(len(setB))

#stores the value by index--no
for x in setB:
    print(x)

    #program 2
    #add()
    setC={11,22,33,44,55}
    setC.add(99)
    print(setC)

    #pop()
    setC.pop()
    print(setC)

    #remove()
    setC.remove(22)
    print(setC)


#union
    setA={1,2,3}
    setB={11,22,33}
    setC=setA.union(setB)
    print(setC)


#intersection
    setE={11,22,33,44}
    setF={44,55,66}
    setG=setE.intersection(setF)
    print(setG)

#intersection_update()
    setE.intersection_update(setF)
    setF.intersection_update(setE)
    print(setE)
    print(setF)
#symmetric_difference()
    setQ={11,22,33}
    setE={23,46,78,33}
    setR=setQ.symmetric_difference(setE)
    print(setR)
#symmetric_difference_update()   
    setQ={11,22,33}
    setE={23,46,78,33}
    setW=setQ.symmetric_difference_update(setE)
    print(setW)
    setR=setE.symmetric_difference_update(setQ)
    print(setR)
#difference()
    setQ={11,22,33}
    setE={34,56,78,33}
    setK=setQ.difference(setE)
    print(setK)
    #difference_update()
    setQ.difference_update(setE)
    print(setQ)
    #issubset()
    setQ={11,22,33}
    setE={11,22,33,44}
    p=setQ.issubset(setE)
    print(p)
    #issuperset()
    p2=setE.issuperset(setQ)
    print(p2)
    #isdisjoint()
    e=setQ.isdisjoint(setF)
    print(e)
    #add()
    setQ.add(55)
    print(setQ)
    #clear()
    setE.clear()
    print(setE)
    #pop()
    setQ.pop()
    print(setQ)
    #rempve()
    setE.remove(44)
    print(setE)
    #update()
    setW.update(5,6,7,8,3)
    print(setW)
    #discard()
    r=setW.discarda(59)
    print(setW)