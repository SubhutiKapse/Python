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